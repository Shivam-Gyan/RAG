from logger import logger

def query_chain(chain, user_input: str):
    try:
        logger.debug(f"Running chain for input: {user_input}")

        # ✅ Use invoke instead of __call__
        result = chain.invoke({"query": user_input})

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
