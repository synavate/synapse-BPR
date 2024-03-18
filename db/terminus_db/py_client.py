import os
from terminusdb_client import WOQLClient
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TERMINUSDB_ACCESS_TOKEN=os.getenv("TERMINUS_ACCESS_TOKEN")
team = os.getenv("TERMINUS_TEAM_URL")

client = WOQLClient("https://cloud.terminusdb.com/snyata|07b1/")
# make sure you have put the token in environment variable
client.connect(team=teamL, use_token=True)

print(client)