from connect import Connect


client = Connect.get_connection()
db = client['sample_airbnb']
col = db['listingsAndReviews']
documents = col.find()

'''print('Printing first 10 documents...')
for doc in documents[:10]:
    country = doc['address']['country']
    name = doc['name']
    print(f'Country: {country}, Name: {name}')'''

#10006546 - 10009999
def print_by_id(id):
    document = col.find_one({'_id':str(id)})
    doc_basic_info = document.get('name'), document.get('room_type'), document.get('price')
    print(doc_basic_info)


# Countries Availables:
#['Portugal', 'Brazil', 'United States', 'Turkey', 'Canada', 'Hong Kong', 'Spain', 'Australia', 'China']
def places_by_country(country, limit):
    selected = col.find({'address.country':country})
    print(f'Printing first {limit} {country} places...')    
    countries = []
    id = 1
    for place in selected[:limit]:
        country = place['address']['country']
        name = place['name']
        city = place['address']['market']
        msg = f'Country: {country} City: {city} Name: {name}'
        countries.append({'id': id, 'country': country, 'city': city, 'name': name})
        id += 1
        
    return countries


def databases():
    names = client.list_database_names()
    db_names = []

    # iterate over the list of database names
    for db_num, db in enumerate(names):
        db_names.append(db)
        # print the database name
        #print ("\nGetting collections for database:", db, "--", db_num)
         
        # use the list_collection_names() method to return collection names
        #collection_names = client[db].list_collection_names()
        #print ("list_collection_names() TYPE:", type(names))
        #print ("The MongoDB database returned", len(collection_names), "collections.")
    
    return ('databases names: ', db_names)
