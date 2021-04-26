import pandas as pd

_date_range = pd.date_range('2021-01-01', periods=12, freq='BM')
#   or
_date_range = pd.date_range('2021', periods=12, freq='BM')
print("_date_range:")
print(_date_range)


