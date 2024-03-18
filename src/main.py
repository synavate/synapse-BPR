from data import
from src.backend.graph.cogdb_operations import CogGraph
from src.backend.graph.user_operations import hashed_user



def main():    
    username = input("What is your username?")
    topic_of_interest = input("What is your topic of interest?")

    user = hashed_user(username, topic_of_interest)





if __name__ == "__main__":
    main()