import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)
print()

_df['Year'] = _df['Date_time'].dt.year

result = _df.groupby(['Year', 'country']).size()
print("result:")
print(type(result))
print(result)
