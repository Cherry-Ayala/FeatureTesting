import os
import json
from pinecone import Index
from openai import AzureOpenAI
from utils import Logger, ToolResult, ToolResultDirection

logger = Logger()



async def _search_tool(
    pinecone_index: Index,
    query: str,
    namespace: str,
    openai_client: AzureOpenAI,
    k: int = 3,
) -> ToolResult:
    logger.info(f"Search tool called with query: {query}")

    try:
        embeddings = openai_client.embeddings.create(
            model=os.getenv("AZURE_EMBEDDINGS_DEPLOYMENT"), input=query
        )
        logger.info("Successfully created embeddings")

        query_embedding = embeddings.data[0].embedding
        search_response = pinecone_index.query(
            namespace=namespace, vector=query_embedding, top_k=k, include_metadata=True
        )
        logger.info(
            f"Pinecone search returned {len(search_response['matches'])} results"
        )

        results = []
        for match in search_response["matches"]:
            results.append(
                {
                    "score": match["score"],
                    "content": match["metadata"].get("text", ""),
                }
            )

        logger.info(f"Returning {len(results)} formatted results")
        return ToolResult(json.dumps(results), ToolResultDirection.TO_SERVER)

    except Exception as e:
        logger.error(f"Error in search tool: {str(e)}")
        return ToolResult(json.dumps({"error": str(e)}), ToolResultDirection.TO_SERVER)
    








    _search_tool()