import os
#from terminusdb_client import Client
from terminusdb_client import WOQLClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TERMINUSDB_ACCESS_TOKEN=os.getenv("TERMINUS_API_TOKEN")
TERMINUS_TEAM_URL = os.getenv("TERMINUS_TEAM_URL")

team = "snyata|07b1"
client = WOQLClient("https://cloud.terminusdb.com/snyata|07b1/")
# make sure you have put the token in environment variable
client.connect(team=team, token=TERMINUSDB_ACCESS_TOKEN, use_token=True)

print(client)