#from pymongo import MongoClient
import pymongo
from datetime import datetime

client = pymongo.MongoClient()
db = client.test
####################
# Find
####################

#result1 = db.restaurants.find({"address.building":"444","grades.score":{"$gte":7, "$lt":10}},{"_id":0, "grades.score":1, "comment":1})
#for document in result1:
    #print(document)

####################
# Update
####################

#db.restaurants.update({"address.building":"444","grades.score":{"$gte":7, "$lt":10}},{"$set":{"comment" : "great!!"}}, multi=True)
#print("---------")

#result1 = db.restaurants.find({"address.building":"444","grades.score":{"$gte":7, "$lt":10}},{"_id":0, "grades.score":1, "comment": 1})
#for document in result1:
    #print(document)

#db.restaurants.update({"address.building":"444","grades.score":{"$gte":7, "$lt":10}},{"$unset":{"comment" : ""}}, multi=True)
#print("---------")

#result1 = db.restaurants.find({"address.building":"444","grades.score":{"$gte":7, "$lt":10}},{"_id":0, "grades.score":1, "comment": 1})
#for document in result1:
    #print(document)

####################
# Regular
####################

#result2 = db.restaurants.find({"address.street":{"$regex":"^\d{3} Avenue$"}},{"_id":0, "address.street":1})
#for document in result2:
    #print(document)

#result2 = db.restaurants.find({"address.street":{"$regex":"^\d{3} Avenue$"}},{"_id":0, "address.street":1})
#for document in result2:
    #print(document)

####################
# Remove
####################

#result2 = db.restaurants.find({"comment":{"$exists":1}})
#for document in result2:
    #print(document)

#db.restaurants.remove({"comment":"great!!"})

#result2 = db.restaurants.find({"comment":{"$exists":1}})
#for document in result2:
    #print(document)

####################
# Group
####################

#result = db.restaurants.aggregate([
    #{"$unwind":"$grades"},
    #{"$group":{"_id":"$cuisine","avg_score":{"$avg":"$grades.score"}}},
    #{"$sort":{"avg_score":1}}
#])
#result = db.restaurants.aggregate([
    #{"$unwind":"$grades"},
    #{"$match": {"grades.score":{"$lt":10}}},
    #{"$group":{"_id":"$cuisine","count":{"$sum":1}}},
    #{"$sort":{"count": -1}}
#])
#result = db.restaurants.aggregate([
    #{"$unwind":"$grades"},
    #{"$group":{"_id":"$cuisine","avg_score":{"$avg":"$grades.score"},"unique_grades":{"$addToSet":"$grades.grade"}}},
#])
#for document in result:
    #print(document)

####################
# GeoIndex
####################

db.restaurants.ensure_index([("address.coord", pymongo.GEO2D)])
result = db.restaurants.find({"address.coord":{"$near":[-73.95, 40.77]}}).limit(10)

for document in result:
    print(document)
