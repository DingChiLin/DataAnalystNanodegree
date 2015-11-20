#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
from datetime import datetime
import xml.etree.cElementTree as ET
from collections import defaultdict
from pprint import pprint
import operator
import re

client = pymongo.MongoClient()
db = client.open_street_map

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
is_english_name = re.compile(r'^([a-zA-Z0-9,\. ]*)$')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def is_problem_key(key):
    m = problemchars.search(key)
    if m and m.group():
        return True
    else:
        return False

def parse_each_tags_in_element(node, element):
    if element.tag == 'way':
        node["node_refs"] = []

    if element.tag == 'relation':
        node["member_refs"] = []

    for child in element:
        if child.tag == 'tag':
            if is_problem_key(child.attrib['k']):
                continue

            addr_in_tags(node, child)
            name_in_tags(node, child)

        elif child.tag == 'nd':
            node["node_refs"].append(child.attrib['ref'])

        elif child.tag == 'member':
            member = {}
            if child.attrib['type']:
                member['type'] = child.attrib['type']
            if child.attrib['ref']:
                member['ref'] = child.attrib['ref']
            if child.attrib['role']:
                member['role'] = child.attrib['role']
            node["member_refs"].append(member)


def addr_in_tags(node, child):

    m = lower_colon.search(child.attrib['k'])
    if m and m.group():
        street_values = m.group().split(":")
        if street_values[0] == 'addr':
            node['address'][street_values[1]] = child.attrib['v']

def name_in_tags(node, child):

    if child.attrib['k'] == 'name':
        node['name']['default'] = child.attrib['v']

    m = lower_colon.search(child.attrib['k'])
    if m and m.group():
        name_values = m.group().split(":")
        if name_values[0] == 'name':
            if 'name' not in node.keys():
                node['name'] = {}

            node['name'][name_values[1]] = child.attrib['v']

def is_in_in_tags_in_element(node, element):
    is_english = False
    have_chinese_is_in_tag = False
    is_in = ''

    for child in element:
        if child.tag == 'tag' and child.attrib['k'] == 'is_in:zh':
            have_chinese_is_in_tag = True
            is_in = child.attrib['v']
            node['is_in'] = child.attrib['v']

    if not have_chinese_is_in_tag:
        for child in element:
            if child.tag == 'tag' and child.attrib['k'] == 'is_in':
                is_in = child.attrib['v']
                node['is_in'] = child.attrib['v']

    if is_in == 'Taipei City, Taiwan':
        node['is_in'] = '台灣台北市'

def nd_in_element(node, element):
    pass

def shape_element(element):
    node = defaultdict(dict)
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
                node['created'][attr] = element.attrib[attr]
            except:
                pass

        #pos
        try:
            node['pos'] = [float(element.attrib['lat']), float(element.attrib['lon'])]
        except:
            pass

        #addr and name
        parse_each_tags_in_element(node, element)

        #is_in
        is_in_in_tags_in_element(node, element)

        #for child in element:
            #if child.tag == 'tag':

                #m1 = problemchars.search(child.attrib['k'])
                #if m1 and m1.group():
                    #continue

                ##address
                #m2 = lower_colon.search(child.attrib['k'])
                #if m2 and m2.group():
                    #street_values = m2.group().split(":")
                    #if street_values[0] == 'addr':
                        #if 'address' not in node.keys():
                            #node['address'] = {}

                        #node['address'][street_values[1]] = child.attrib['v']
                        #continue

                #node[child.attrib['k']] = child.attrib['v']

                ##name

            #elif child.tag == 'nd':
                #if 'node_refs' not in node.keys():
                    #node['node_refs'] = []

                #node["node_refs"].append(child.attrib['ref'])

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

    result = db.taipei_street.find({'is_in':{"$exists":1}},{'is_in':1})
    for document in result:
        print(document)


process_map('taipei_city_taiwan.osm')
