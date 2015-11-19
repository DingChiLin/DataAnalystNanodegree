import pymongo
from datetime import datetime

client = pymongo.MongoClient()
db = client.arthur

db.friends.remove()

db.friends.insert([{'name':'stone', 'age':100, 'status':'A'}, {'name':'molly', 'age':10}, {'name':'kevin', 'age':22}])
result = db.friends.find()
for document in result:
    print(document)
