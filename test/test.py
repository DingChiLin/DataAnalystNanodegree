from pandas import DataFrame, Series
import numpy

def add5(x):
  return x+5

year = Series([2012,2013,2014])
name = Series(['Arthur','Molly','Stone'])
wins = Series([7,8,9])
data = {'year':year,
        'name':name,
        'wins':wins}
d = DataFrame(data)
print d
print '1----'
print d.loc[0]
print '2----'
print d[d.wins>7]
print '3----'
print d.name[d.wins+d.year>2010]
print '4----'
print map(add5, d.wins)
print '5----'
print d[['year','wins']]
print len(d.index)



arr = [1,2,3,4,5]
print arr - 1
