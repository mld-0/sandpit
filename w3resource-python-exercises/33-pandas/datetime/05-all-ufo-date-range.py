import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace("24:", "00:")
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format="%m/%d/%Y %H:%M")

print("_df:")
print(_df)
print()

_date_start = '1950-10-10'
_date_end = '1960-10-10'

#   With datetime as field
result = _df[(_df['Date_time'] >= _date_start) & (_df['Date_time'] <= _date_end)]
#   or
result = _df.query('Date_time >= @_date_start & Date_time <= @_date_end')
print("result:")
print(result)
print()

#   With datetime as index
_df = _df.set_index(['Date_time']).sort_index()  # DataFrame should be sorted in order to slice by datetime index
result = _df.loc[_date_start:_date_end]
print("result:")
print(result)

