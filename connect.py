from pymongo import MongoClient
import certifi


with open('./access_key.txt') as f:
    DB_ACCESS = f.read().strip()


class Connect(object):
    @staticmethod    
    def get_connection():
        return MongoClient(DB_ACCESS, tlsCAFile=certifi.where())
