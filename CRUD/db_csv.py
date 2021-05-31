from connect import Connect
import csv
import os


#get connection
client = Connect.get_connection()


curr_dir = os.getcwd()
#CSV to JSON Conversion
def insert_csv_data(collection, filename):
    with open(curr_dir + '/samples/' + filename , 'r') as csvfile:
        reader = csv.DictReader( csvfile )
        #header = [ "ean", "category", "name", "price", "quantity", "real_price", "store_id", "sale_type", "unit_type", "typestore", "typestorename"]
        #header = ['id', 'name', 'typestore', 'typestorename']
        header = reader.fieldnames

        for each in reader:
            row={}
            for field in header:
                row[field]=each[field]

            #db.segment.insert(row)
            collection.insert(row)


#def insert_csv_data(collection):
    # Inserting both document one by one
#    collection.insert_one()


#create a dabase + collection
def create_db():
    db = client['price_analytics']
    
    collection = db['stores']
    insert_csv_data(collection, 'store_v1(small).csv')

    collection = db['products']
    insert_csv_data(collection, 'products_v1(small).csv')

