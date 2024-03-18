import os
import sys

from dotenv import load_dotenv, find_dotenv
from qdrant_client import QdrantClient
from loguru import logger

load_dotenv(find_dotenv())
logger.add("../logs/db/file_{time}.log")
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

def auth_dbs():
    try:
        ### QDRANT CLIENT ###
        qdrant_client = QdrantClient(
            url="https://b94c5565-cf5e-446f-b488-9282179598b8.us-east4-0.gcp.cloud.qdrant.io:6333", 
            api_key=os.getenv("QDRANT_API_KEY"),
        )
        logger.info("Qdrant client created")
        ### MONGO CLIENT ###
        mongo_client = 
        
        ###TerminusDBClient
        
    except ConnectionError as e:
        logger.error("Error %s", e)
    



if __name__=="__main__":
    main()