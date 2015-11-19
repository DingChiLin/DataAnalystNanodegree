import xml.etree.cElementTree as ET
from collections import defaultdict
from pprint import pprint
import operator

def process_map(file_in):
    # You do not need to change this file
    data = defaultdict(int)
    for _, element in ET.iterparse(file_in):
        data[element.tag] += 1

    print(data)
