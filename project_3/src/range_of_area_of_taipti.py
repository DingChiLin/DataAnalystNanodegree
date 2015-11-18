import xml.etree.cElementTree as ET
from collections import defaultdict
from pprint import pprint
import operator

min_lat=24.8615
max_lat=25.2143
min_lon=121.2678
max_lon=121.8590

def process_map(file_in):
    # You do not need to change this file
    data = []
    for _, element in ET.iterparse(file_in):
        if element.tag == 'node':
            lat = float(element.attrib['lat'])
            lon = float(element.attrib['lon'])

            if lat < min_lat or \
               lat > max_lat or \
               lon < min_lon or \
               lon > max_lon:
                data.append(element)

    print(len(data))

process_map('taipei_city_taiwan.osm')
