from fastapi import FastAPI,UploadFile,File,Form,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Optional

from langchain_chroma import Chroma
from modules.load_vectorstore import load_vectorstore
from modules.llm import get_llm_chain
from modules.query_handlers import query_chain
from modules.pdf_handlers import save_uploaded_files
from logger import logger


app = FastAPI()


# allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=3600,
)

@app.middleware("http")
async def catch_exception_middleware(request:Request,call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        logger.exception("UNHANDLED EXCEPTION")
        return JSONResponse(status_code=500,content={"error":str(exc)})

@app.post('/upload_pdfs')
async def upload_pdfs(files:List[UploadFile]=File(...)):
    try:
        logger.info(f"Received {len(files)} files for upload.")
        load_vectorstore(files)
        logger.info("Vectorstore loaded successfully.")
        return {"message":"Files uploaded and vectorstore updated successfully."}
    except Exception as e:
        logger.exception("Error in /upload_pdfs")
        return JSONResponse(status_code=500,content={"error":str(e)})

# @app.post('/query')
# async def ask_question(question:str=Form(...)):
#     try:
#         logger.info(f"Received query: {question}")
#         from langchain_chroma import Chroma
#         # from langchain_community.vectorstores import Chroma
#         from langchain_google_genai import GoogleGenerativeAIEmbeddings
#         from modules.load_vectorstore import PERSIST_DIR, UPLOAD_DIR

#         embed_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         vectorstore = Chroma(
#             embedding_function=embed_model,
#             persist_directory=PERSIST_DIR
#         )
#         chain = get_llm_chain(vectorstore)
#         result = query_chain(chain, question)
#         logger.info(f"Query result: {result}")
#         # response = {
#         #     "response": result["response"],
#         #     "sources": result["sources"]
#         # }
#         logger.info("Query processed successfully.")
#         return result
#     except Exception as e:
#         logger.exception("Error in /query")
#         return JSONResponse(status_code=500,content={"error":str(e)})
    
@app.post('/query')
async def ask_question(question: str = Form(...)):
    try:
        logger.info(f"Received query: {question}")
        from modules.load_vectorstore import PERSIST_DIR
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        from langchain_chroma import Chroma

        embed_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        # ✅ Correct way: load persisted Chroma
        vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embed_model
        )

        # Build chain
        chain = get_llm_chain(vectorstore)

        # Run query
        result = query_chain(chain, question)
        logger.info(f"Query result: {result}")
        return result
    except Exception as e:
        logger.exception("Error in /query")
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/")
def read_root():
    return {"hello world": "This is a FastAPI application."}