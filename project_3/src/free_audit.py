import xml.etree.cElementTree as ET
from collections import defaultdict
from pprint import pprint
import operator

def process_map(file_in):
    # You do not need to change this file
    data = defaultdict(int)
    for _, element in ET.iterparse(file_in):
        if element.tag == 'tag':
            if element.attrib['k'] == 'highway':
                data[element.attrib['v']] += 1

    data = sorted(data.items(), key=operator.itemgetter(1))
    pprint(data)

process_map('taipei_city_taiwan.osm')
