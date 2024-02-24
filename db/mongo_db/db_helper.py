''' Can we keep the information discused on track and where it is reprompt it? Who knows 
but we'll save files to a MongoDB service'''

import os
import pymongo
import datetime

class DBOps:
    """ functions for performing basic database operations during a debate based on MongoDB"""
 
 
    def __init__(self, add, port):
        pass
    

    def open_connection():
        pass

    def close_connection():
        pass

#All methods need tending to with credentials and paths etc
class DebateMonitor:


    def __init__(self, db_uri, db_name):
        self.client = pymongo.MongoClient(db_uri)
        self.db = self.client[db_name]
        self.questions_collection = self.db['questions']
        self.answers_collection = self.db["answers"]
    
    def record_question(self, text ,topic):
        question_data = {"text":text,
                         "timestamp":datetime.now(),
                         "topic":topic,
                         "answers": []
                         }
        result = self.questions_collection.insert_one(question_data)
        return  result.inserted_id

    def record_answer(self, question_id, participant, text, sentiment):
        answer_data = { "question_id": question_id,
                       "speaker": speaker.name,
                        "text": text,
                       "timestamp": datetime.now,
                       "sentiment": sentiment
                       }
        self.answers_collection.insert_one(answer_data)
        return result.inserted_id

    def update_qa(self, question_id, answer_id):
        pass

    def get_questions(self):
        return list(self.questions_collection.find())
    
    def get_answersa(self):
        return list(self.answers_collection.find())
    
