import numpy
import scipy.stats
import pandas

f_in = open('baseball_stats.csv','r')
baseball_data = pandas.read_csv(f_in, delimiter=",")
right_player = baseball_data[baseball_data.handedness == 'R']
left_player = baseball_data[baseball_data.handedness == 'L']

result = scipy.stats.ttest_ind(right_player.avg,left_player.avg,equal_var=False)
print (result[1] < 0.05, result)

arr = []
for i in range(0,len(baseball_data.index)):
    arr.append(i)

print ((baseball_data.avg - 20)**2).sum()
print baseball_data.avg - arr
