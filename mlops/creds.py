import os
import openai
from dotenv import load_dotenv, find_dotenv
from typing import List, Union, Tuple, Dict

load_dotenv(find_dotenv())
_llm_creds: Dict = {}
_mlops_creds: Dict = {}
_svc_config: Dict = {}

project_mlops = []


#List of llm configs
llm_creds["openai_api_key"] = os.getenv("OPENAI_API_KEY")

#list of mlops
mlops_creds["humanloop_api"] = os.getenv("OPENAI_API_KEY")
mlops_creds = os.getenv("WANDB_API_KEY")
mlops_creds = os.getenv("MLFLOW_API_KEY")
#mlops_creds = os.getenv("")
#mlops_creds = os.getenv("")
#mlops_creds = os.getenv("")
#mlops_creds = os.getenv("")
#mlops_creds = os.getenv("")


#Host config
mlflow_

    
    
