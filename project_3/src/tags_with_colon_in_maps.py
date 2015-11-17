import xml.etree.cElementTree as ET
from collections import defaultdict
from pprint import pprint
import operator
import re

name_with_colon = re.compile(r'^(\w*):(\w*)$')

def process_map(file_in):
    # You do not need to change this file
    data = defaultdict(int)
    for _, element in ET.iterparse(file_in):
        if element.tag == 'tag':
            m = name_with_colon.search(element.attrib['k'])
            if m and m.group():
                if m.group(1) != 'addr' and \
                   m.group(1) != 'name' and \
                   m.group(1) != 'old_name' and \
                   m.group(1) != 'alt_name' and \
                   m.group(2) != 'en' and \
                   m.group(2) != 'zh':

                    data[m.group()] += 1

    data = sorted(data.items(), key=operator.itemgetter(1))
    pprint(data)
    print(len(data))


process_map('taipei_city_taiwan.osm')
