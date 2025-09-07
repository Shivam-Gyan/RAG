from logger import logger

def query_chain(chain, question: str):
    try:
        logger.debug(f"Running chain for input: {question}")

        # ✅ Use correct input key
        result = chain.invoke({"query": question})
        

        # Log context for debugging
        for i, doc in enumerate(result.get("source_documents", [])):
            logger.debug(f"Doc {i} content preview: {doc.page_content[:500]}")

        response = {
            "response": result["result"],
            "sources": [
                doc.metadata.get("source", "")
                for doc in result.get("source_documents", [])
            ]
        }

        logger.debug(f"Chain response: {response}")
        return response

    except Exception as e:
        logger.exception("Error in query_chain")
        raise
