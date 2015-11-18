import xml.etree.cElementTree as ET
from collections import defaultdict
from pprint import pprint
import operator
import re

name_with_colon = re.compile(r'^(\w*):(\w*)$')
is_english_name = re.compile(r'^([a-zA-Z0-9,\. ]*)$')

def process_map(file_in):
    # You do not need to change this file
    data = defaultdict(int)
    for _, element in ET.iterparse(file_in):
        if element.tag == 'relation':
            is_english = False
            for child in element:
                if child.tag == 'tag' and child.attrib['k'] == 'is_in':
                    m = is_english_name.search(child.attrib['v'])
                    if m and m.group():
                        is_english = True
                    else:
                        data[child.attrib['v']] += 1

            if is_english:
                for child in element:
                    if child.tag == 'tag' and child.attrib['k'] == 'is_in:zh':
                        data[child.attrib['v']] += 1


    data = sorted(data.items(), key=operator.itemgetter(1))
    pprint(data)
    print(len(data))


process_map('taipei_city_taiwan.osm')
