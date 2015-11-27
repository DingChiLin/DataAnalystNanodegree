import pymongo
import pandas as pd

client = pymongo.MongoClient()
db = client.open_street_map

#for x in db.taipei_street.find():
    #x['created']['version'] = int(x['created']['version']);
    #db.taipei_street.save(x);
result = db.taipei_street.aggregate([{"$group":{"_id":"$created.version", "count":{"$sum":1}}},{"$sort":{"_id":-1}},{"$limit":1}])

#result = db.taipei_street.find().limit(1)
for document in result:
    print(document)

