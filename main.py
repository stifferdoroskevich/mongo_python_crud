import json
from CRUD import db_csv, db_read, db_create

# Database in cloud.mongodb.com
# Data samples by cloud.mongodb


#create database_sample + collection sample + inserts 2 documents
db_create.create_db()

#create price_analytics + collections (stores, products) + inserts data from csv files
db_csv.create_db()

#return list of databases
print(db_read.databases())

# Print List of places by country.
countries = db_read.places_by_country('Spain', 7)
json_formatted_str = json.dumps(countries, indent=2)
print(json_formatted_str)
