from nest.core.database.base_odm import OdmService
from src.examples.examples_entity import Examples
import os
from dotenv import load_dotenv

load_dotenv()
    

config = OdmService(
    db_type="mongodb",
    config_params={
        "db_name": os.getenv("DB_NAME"),
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "port": os.getenv("DB_PORT"),
    },
    document_models=[Examples]
)       
        