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
