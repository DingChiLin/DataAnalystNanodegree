import pymongo
from datetime import datetime
import xml.etree.cElementTree as ET
from collections import defaultdict
from pprint import pprint
import operator

client = pymongo.MongoClient()
db = client.taipei_street

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way" or element.tag == 'relation':

        #id
        node['id'] = element.attrib['id']

        #type
        node['type'] = element.tag

        #visible
        try:
            node['visible'] = element.attrib['visible']
        except:
            pass

        #created
        for attr in CREATED:
            try:
                if 'created' not in node.keys():
                    node['created'] = {}

                node['created'][attr] = element.attrib[attr]
            except:
                pass

        #pos
        try:
            node['pos'] = [float(element.attrib['lat']), float(element.attrib['lon'])]
        except:
            pass

        return node
    else:
        return None

def process_map(file_in):
    data = []
    for _, element in ET.iterparse(file_in):
        el = shape_element(element)
        if el:
            data.append(el)

    insert(data)


def insert(data):
    db.taipei_street.remove()
    db.taipei_street.insert(data)

    result = db.taipei_street.find()
    for document in result:
        print(document)


process_map('taipei_city_taiwan_min.osm')
