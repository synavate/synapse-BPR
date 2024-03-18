import os
from dotenv import load_dotenv, find_dotenv
from cog.torque import Graph

class CogGraph:
    """ A utility class to generate a cog for prototyping"""
    def __init__(self, user):
        self.name_graph = user[0][hash]
        self.gr = Graph(graph_name=self.name_graph, cog_home='./')
        
    def extract_info_from_source(self, data, v1, predicate, v2):
        
    
        
    
        
        
