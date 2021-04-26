import pandas as pd
import datetime

today = datetime.datetime(2012, 10, 30)
print("Current date:", today)

tomorrow = today + pd.Timedelta(days=1)
print("Tomorrow:", tomorrow)

yesterday = today - pd.Timedelta(days=1)
print("Yesterday:", yesterday)

date1 = datetime.datetime(2016, 8, 2)
date2 = datetime.datetime(2016, 7, 19)
_delta_date12 = date1 - date2
print("Difference between two dates: ", _delta_date12)

