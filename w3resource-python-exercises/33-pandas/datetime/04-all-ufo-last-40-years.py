import datetime
import dateutil
import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = pd.to_datetime(_df['Date_time'].str.replace("24:", "00:"), format="%m/%d/%Y %H:%M")

print("_df:")
print(_df)
print()

_now = datetime.datetime.now()
print("_now:")
print(type(_now))
print(_now)
print()

_40_years_ago = _now - relativedelta(years=40)
print("_40_years_ago:")
print(_40_years_ago)

result = _df[_df['Date_time'] >= _40_years_ago]
print("result:")
print(result)

