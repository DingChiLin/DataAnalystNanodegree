import pandas as pd
import numpy as np

filename = 'pisa2012_clean.csv'

f_in = open(filename,'r')
df = pd.read_csv(f_in, delimiter=",")

print(df['LanguageLearningTime'])

grouped = df.groupby('Country')
transformed_data = grouped.agg({'Weight':sum})
for col_name in df.columns.values:
    if col_name != 'index' and col_name != 'Country' and col_name != 'Weight':
        transformed_data[col_name] = grouped.apply(lambda x: np.average(x[col_name], weights=x['Weight']))

transformed_data['ICTResourcesClass'] = pd.cut(transformed_data['ICTResources'], 5, labels=['E','D','C','B','A'])

transformed_data.to_csv('pisa2012_transform.csv', sep=',', index_label='Country')
