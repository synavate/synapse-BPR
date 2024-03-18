# RAG Pipeline using PDF sources
import os
from loguru import logger as _logger
from dotenv import load_dotenv, find_dotenv
from db.mongo_db.mongo_qa import MongoDB
from llamaindex.core import PDFReader


load_dotenv(find_dotenv())

"""
Utility Methods: docs0[94].get_content()
"""


SOURCE = "MONGODB" | "LOCAL" | None
DEBUG = True

if SOURCE == "LOCAL":
    files = []
elif SOURCE == "MONGODB":  
    try:
        mongo_client = MongoDB()
        _logger.info("MongoDB client created")
    except Exception as e:
        _logger.error(e)
        SOURCE = "LOCAL"


loader = PDFReader()
docs0 = loader.load_data(file=Path("/content/State of AI Report 2023 - ONLINE.pdf"))