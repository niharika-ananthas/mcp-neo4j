from mcp.server.fastmcp import FastMCP
import os
from llm_connect import llmConnection
from graph_db_connect import graphDBConnect
from neo4j_graphrag.embeddings.openai import AzureOpenAIEmbeddings
from neo4j_graphrag.retrievers import VectorRetriever
from neo4j_graphrag.llm import AzureOpenAILLM
from neo4j_graphrag.generation.graphrag import GraphRAG

host = os.environ["mcp_server_host"]
port = os.environ["mcp_server_port"]

mcp = FastMCP("mcp", host=host, port = port)

@mcp.tool()
def generate_cypher(user_prompt:str)->str:
    """Generate Cypher query from user input"""
    llm_connector = llmConnection()
    llm_driver = llm_connector.create_llmConnection()
    response = llm_driver.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content": "You are a helpful assistant."
                "Please convert prompt to CYpher query and return only Cypher query."
                "Ignore the case of alphabets in the search text."
            },
            {
                "role":"user",
                "content": user_prompt,                 
            }
        ],
        model=os.environ["deployment"]
    )
    query = response.choices[0].message.content
    return query

@mcp.tool()
def graphdb_connect(query: str)->str:
    """Connect tp graph database and execute a cypher query and return results."""
    graph_connector = graphDBConnect()
    graph = graph_connector.create_graphDBConnect()
    response = graph.execute_query(query)
    return response

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
