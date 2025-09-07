from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from logger import logger
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_llm_chain(vectorstore):
    # Define LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2  # ✅ Low temp → factual answers
    )

    # Define Prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are **MediBot**, an AI-powered assistant trained to help users understand medical documents and health-related questions.

Your job is to provide clear, accurate, and helpful responses based **only on the provided context**.

---

🔍 **Context**:
{context}

🙋‍♂️ **User Question**:
{question}

---

💬 **Answer**:
- Respond in a calm, factual, and respectful tone.
- Use simple explanations when needed.
- If the context does not contain the answer, say: "I'm sorry, but I couldn't find relevant information in the provided documents."
- Do NOT make up facts.
- Do NOT give medical advice or diagnoses.
"""
    )

    # Build RetrievalQA Chain
    # retriever = vectorstore.as_retriever(search_kwargs={"k":3})
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke("test")
    logger.info(f"Retriever pulled {len(docs)} docs")
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # ✅ simplest: stuff all docs into context
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
        verbose=True  # ✅ helpful for debugging
    )
