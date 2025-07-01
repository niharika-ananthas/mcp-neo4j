import os
from neo4j import GraphDatabase

class graphDBConnect():
    def __init__(self):
        self.url=os.environ["db_url"]
        self.un=os.environ["db_un"]
        self.key=os.environ["db_key"]

    def create_graphDBConnect(self):
        try:
            graphdb_driver = GraphDatabase.driver(uri=self.url,
                                                  auth=(self.un,self.key),encrypted=True)
            try:
                graphdb_driver.verify_connectivity()
                print("Connnected Succesfully")
            except Exception as e:
                print("Error connecting graphDatabase", e)
            return graphdb_driver
        except Exception as e:
            print("Error connecting graphDatabase", e)