import pymongo
import pandas as pd
from ggplot import *

client = pymongo.MongoClient()
db = client.open_street_map

result = db.taipei_street.aggregate([{"$group":{"_id":"$created.user", "count":{"$sum":1}}}, {"$sort":{'count':-1}}])

data = {}
data['rank'] = []
data['contributions'] = []

i = 0
for document in result:
    i += 1

    if i >= 30:
        break

    data['rank'].append(i)
    data['contributions'].append(document['count'])



df = pd.DataFrame(data)
print(df)

p = ggplot(data, aes('rank', 'contributions')) + geom_bar(stat="identity") + xlim(0, 30)
print(p)
#p = ggplot( df, aes( 'prediction', 'standardized_residual') ) + ggtitle( 'standardized_residual vs prediction' ) + geom_point( color = "red" )
#print(p)
