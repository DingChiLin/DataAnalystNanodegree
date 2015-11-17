import string
#myStr = "Hello, World!"
#print(myStr)
#exclude = set(string.punctuation)
#print(exclude)

#arr = ['1','2','3','4','5']
#print(arr)
#for a in arr:
    #print a

#arr2 = "".join(c for c in arr)
#print(arr2)

#h = {}
#h['a'] = 'A'
#h['b'] = 'B'

#if 'a' in h:
    #print "AAA".lower()

#if 'c' in h:
    #print "CCC"

#arr3 = [1,2]
#a,b = arr3
#print a

str = ' mar.serre@[upc.edu] 1['
remove = '!"#$%&\'()*+,-/:;<=>?\[\]^_`{|}~ '
s = str.translate(None, remove)
print(s)
