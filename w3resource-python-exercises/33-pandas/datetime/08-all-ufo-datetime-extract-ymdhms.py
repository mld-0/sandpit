import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)
print()

result = pd.DataFrame()
result['year'] = _df['Date_time'].dt.year
result['month'] = _df['Date_time'].dt.month
result['day'] = _df['Date_time'].dt.day
result['hour'] = _df['Date_time'].dt.hour
result['min'] = _df['Date_time'].dt.minute
result['sec'] = _df['Date_time'].dt.second
result['weekday'] = _df['Date_time'].dt.day_name()

print("result:")
print(result)

