import pandas as pd

_start_dates = pd.date_range('2020-01-01', '2020-12-31', freq='BQS')
_end_dates = pd.date_range('2020-01-01', '2020-12-31', freq='BQ')

print("_start_dates:")
print(_start_dates)

print("_end_dates:")
print(_end_dates)

