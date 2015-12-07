import googlemaps
from pprint import pprint
from math import radians, cos, sin, asin, sqrt


API_KEY = 'AIzaSyCwEShCrrq2WcigAnkZSfZfWIJyRCCPk0w'
address = "臺北市大同區長安西路226號"
#address2 = '臺北市中山區力行里長安東路二段165號'
#address3 = '新北市永和區頂溪里永和路二段303號'
#address4 = '臺北市大同區景興里延平北路三段2號'

gmaps = googlemaps.Client(API_KEY)
geocode_result = gmaps.geocode(address)

pprint(geocode_result)

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

print(haversine(25.0493618, 121.5168299, 24.9936329, 121.539171))

