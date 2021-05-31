from connect import Connect
import test_data



def insert_test_data(collection):
    # Inserting both document one by one
    collection.insert_one(test_data.document1)
    collection.insert_one(test_data.document2)

#create a dabase + collection
def create_db():
    client = Connect.get_connection()
    db = client['db_sample']
    collection = db['collection_sample']
    
    insert_test_data(collection)





