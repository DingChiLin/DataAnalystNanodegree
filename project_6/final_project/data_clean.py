import pandas as pd

filename = 'pisa2012.csv'

f_in = open(filename,'r')
df = pd.read_csv(f_in, delimiter=",")
clean_data = df[['CNT','ST01Q01','ST02Q01','ST04Q01']]
df.rename(columns={'CNT': 'Country', 'ST01Q01': 'Grade'}, inplace=True)
print(clean_data)
