#!/usr/bin/python

import sys
import pickle

sys.path.append("./")
from poi_email_addresses import poiEmails


sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary'] # You will need to use more features

### Load the dictionary containing the dataset
with open("../final_project/final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

print(len(data_dict))

print(len(poiEmails()))

poi_email_in_data=[]
all_email_in_data=[]
for name, features in data_dict.iteritems():
    print(name)
    email = features['email_address']
    all_email_in_data.append(email)

    if(features['poi']):
        if(email in poiEmails()):
            poi_email_in_data.append(email)
            #print(email)
            #print('1: poi in poi_email_list')
        else:
            print('2: poi not in poi_email_list')

    else:
        if(email in poiEmails()):
            print('3: not poi in poi_email_list')

###
print('############')

from os import walk

f = []
mypath = './emails_by_address'
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

from_emails = []
to_emails = []
for filename in f:
    if(filename[:3] == 'to_'):
        to_emails.append(filename[3:-4])
    elif(filename[:5] == 'from_'):
        from_emails.append(filename[5:-4])

all_poi_emails = []
for t_email in to_emails:
    if (t_email in poiEmails()) or (t_email in poi_email_in_data):
        all_poi_emails.append(t_email)

all_emails = []
for t_email in to_emails:
    if (t_email in poiEmails()) or (t_email in all_email_in_data):
        all_emails.append(t_email)


print(len(all_poi_emails))
print(len(all_emails))
print('&&&&&&&&')

poi_to_email_count = 0
non_poi_to_email_count = 0
poi_from_email_count = 0
non_poi_from_email_count = 0

for email in all_emails:
    to_filename = 'to_' + email + '.txt'
    from_filename = 'from_' + email + '.txt'

    to_num_lines = sum(1 for line in open('emails_by_address/' + to_filename))
    from_num_lines = sum(1 for line in open('emails_by_address/' + from_filename))
    
    if email in all_poi_emails:
        poi_to_email_count += to_num_lines
        poi_from_email_count += from_num_lines
    else:
        non_poi_to_email_count += to_num_lines
        non_poi_from_email_count += from_num_lines


print(poi_to_email_count)
print(non_poi_to_email_count)
print(poi_from_email_count)
print(non_poi_from_email_count)


#with open("emails_name_by_address.txt",'w') as file:
    #for item in to_emails:
        #print>>file, item




