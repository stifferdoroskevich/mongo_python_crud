import json
from CRUD import db_read


#print_by_id(10006546)
#print_by_country('Portugal', 5)

# ['Portugal', 'Brazil', 'United States', 'Turkey', 'Canada', 'Hong Kong', 'Spain', 'Australia', 'China']
countries = db_read.places_by_country('Spain', 3)
json_formatted_str = json.dumps(countries, indent=2)
print(json_formatted_str)


