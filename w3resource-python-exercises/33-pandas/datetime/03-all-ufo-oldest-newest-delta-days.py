import datetime
import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format="%m/%d/%Y %H:%M")
#_df['Date_time'] = pd.to_datetime(_df['Date_time'])

print("_df:")
print(_df)
print()

_today = datetime.date.today()
_today_str = _today.strftime('%F')

_date_newest = _df['Date_time'].max()
_date_oldest = _df['Date_time'].min()

print("_date_newest:")
print(_date_newest)
print("_date_oldest:")
print(_date_oldest)
print()

_delta = _date_newest - _date_oldest
print("_delta:")
print(type(_delta))
print(_delta)
print()

_delta_days = _delta.days
print("_delta_days:")
print(type(_delta_days))
print(_delta_days)

