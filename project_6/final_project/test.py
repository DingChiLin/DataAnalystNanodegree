import pandas as pd

filename = 'pisa2012_clean.csv'

f_in = open(filename,'r')
df = pd.read_csv(f_in, delimiter=",")
df=df.dropna()
df.to_csv('pisa2012_clean_2.csv', sep=',')
