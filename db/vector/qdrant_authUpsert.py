import os
from dotenv import load_dotenv, find_dotenv
from qdrant_client import QdrantClient

load_dotenv(find_dotenv())

qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"), 
    api_key=os.getenv("QDRANT_API_KEY"),
)

print(qdrant_client)
