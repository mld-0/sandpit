import datetime
import dateutil
import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)

#   Using timedelta (map is slower than addition series addition)
result = _df['Date_time'].map(lambda x: x + datetime.timedelta(days=180))
result = _df['Date_time'] + datetime.timedelta(days=180) 
#   Using relativedelta
result = _df['Date_time'].map(lambda x: x + dateutil.relativedelta.relativedelta(days=180))

print("result:")
print(result)
