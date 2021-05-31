import json
from CRUD import db_read, db_create


# create database_sample + collection sample + inserts 2 documents
db_create.create_db()
print(db_read.databases())

#Print List of places by country.
#Countries Availables:
#['Portugal', 'Brazil', 'United States', 'Turkey', 'Canada', 'Hong Kong', 'Spain', 'Australia', 'China']
countries = db_read.places_by_country('Spain', 7)
json_formatted_str = json.dumps(countries, indent=2)
print(json_formatted_str)
