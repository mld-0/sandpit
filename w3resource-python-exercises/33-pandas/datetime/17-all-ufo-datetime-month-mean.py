import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')

_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
_df['date_documented'] = pd.to_datetime(_df['date_documented'], format='%m/%d/%Y')
print("_df:")
print(_df)
print()

_df = _df.set_index(_df['date_documented'], drop=True)
_df['month_documented'] = _df['date_documented'].apply(lambda x: x.month)

#result = _df.groupby(['month_documented']).size()
#print("result:")
#print(result)
#
