import pymongo
from pprint import pprint
import googlemaps
import re
from math import radians, cos, sin, asin, sqrt

#API_KEY = 'AIzaSyCwEShCrrq2WcigAnkZSfZfWIJyRCCPk0w'
API_KEY = 'AIzaSyCKwvKi7V3imhpBemgqOnwLetvhjC3vjLE'

client = pymongo.MongoClient()
db = client.open_street_map
result = db.taipei_street.find({"type":'node', "address.full":{"$exists":1}},{"_id":0, "pos":1, "address.full":1})

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

multiple_locations = 0
same_position = 0
no_location = 0
no_address = 0

location_deviation = 0
location_huge_deviation = 0

count = 0

for document in result:
    count += 1
    print(count)

    address = document['address']['full']
    m = re.compile(r'^([\w\s,、.-]*號)[\w\s\(\);,、.-]*$').search(address)
    if m and m.group(1):
        address = m.group(1)
    else:
        no_address += 1
        continue

    coordinate_openstreetmap = document['pos']

    try:
        gmaps = googlemaps.Client(API_KEY)
        geocode_result = gmaps.geocode(address)

        if len(geocode_result) > 1:
            multiple_locations += 1

        location = geocode_result[0]['geometry']['location']
        coordinate_google = [location['lat'], location['lng']]

        distance = haversine(coordinate_google[0], coordinate_google[1], coordinate_openstreetmap[0], coordinate_openstreetmap[1])
        if distance >= 1:
            print("location huge deviation")
            print(address)
            print(distance)
            location_huge_deviation += 1
        elif distance >= 0.5:
            print("location  deviation")
            print(address)
            print(distance)
            location_deviation += 1

        if abs(coordinate_google[0] - coordinate_openstreetmap[0]) <= 0.000001 and \
           abs(coordinate_google[1] - coordinate_openstreetmap[1]) <= 0.000001:
            same_position += 1
            print("same location")
            print(address)
            print(coordinate_google)
            print(coordinate_openstreetmap)

    except:
        no_location += 1
        print("no location")
        print(address)

print('conclusion')
print(multiple_locations)
print(same_position)
print(no_location)
print(no_address)
print(location_deviation)
print(location_huge_deviation)
