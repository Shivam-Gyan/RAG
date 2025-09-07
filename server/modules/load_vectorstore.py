import os
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain.vectorstores import Chroma
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
# from pinecone import Pinecone, ServerlessSpec   # 🔹 keep Pinecone import (commented)

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# PINECONE_ENV = "us-east-1"
# PINECONE_INDEX_NAME = "medical-index"

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

PERSIST_DIR = "./chroma_db"
UPLOAD_DIR = "./uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# -------------------------------
# (Optional) Initialize Pinecone
# -------------------------------
# pc = Pinecone(api_key=PINECONE_API_KEY)
# spec = ServerlessSpec(cloud="aws", region=PINECONE_ENV)
# existing_indexes = [i["name"] for i in pc.list_indexes()]
#
# if PINECONE_INDEX_NAME not in existing_indexes:
#     pc.create_index(
#         name=PINECONE_INDEX_NAME,
#         dimension=768,  # For GoogleGenerativeAI embeddings
#         metric="dotproduct",
#         spec=spec
#     )
#     while not pc.describe_index(PINECONE_INDEX_NAME).status["ready"]:
#         time.sleep(1)
#
# index = pc.Index(PINECONE_INDEX_NAME)

# -------------------------------
# Load, split, embed and store in Chroma
# -------------------------------
def load_vectorstore(uploaded_files):
    embed_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # ✅ Save uploaded files and collect paths in one pass
    file_paths = []
    for file in uploaded_files:
        save_path = Path(UPLOAD_DIR) / file.filename
        with open(save_path, "wb") as f:
            f.write(file.file.read())
        file_paths.append(str(save_path))

    # ✅ Load all documents from all files
    all_documents = []
    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        all_documents.extend(loader.load())

    if not all_documents:
        print("⚠️ No text extracted from uploaded PDFs. Skipping.")
        return None

    # ✅ Split into chunks once
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(all_documents)

    if not chunks:
        print("⚠️ No chunks to embed after splitting. Skipping.")
        return None

    print(f"🔍 Preparing {len(chunks)} chunks for embedding...")

    # -------------------------------
    # ✅ Use Chroma (local vectorstore)
    # -------------------------------
    if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        vectorstore = Chroma(
            embedding_function=embed_model,
            persist_directory=PERSIST_DIR
        )
        vectorstore.add_documents(chunks)
    else:
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embed_model,
            persist_directory=PERSIST_DIR
        )

    # vectorstore.persist()
    print(f"✅ Chroma DB updated at {PERSIST_DIR}")

    # -------------------------------
    # 🔹 Alternative: Pinecone (remote vectorstore)
    # -------------------------------
    # texts = [chunk.page_content for chunk in chunks]
    # metadatas = [chunk.metadata for chunk in chunks]
    # ids = [f"{Path(chunk.metadata.get('source', 'doc')).stem}-{i}" for i in range(len(chunks))]
    #
    # embeddings = embed_model.embed_documents(texts)
    #
    # vectors = [
    #     {
    #         "id": ids[i],
    #         "values": embeddings[i],
    #         "metadata": metadatas[i]
    #     }
    #     for i in range(len(embeddings))
    # ]
    #
    # print("📤 Uploading to Pinecone...")
    # with tqdm(total=len(vectors), desc="Upserting to Pinecone") as progress:
    #     index.upsert(vectors=vectors)
    #     progress.update(len(vectors))
    #
    # print("✅ Upload complete to Pinecone")

    return vectorstore
