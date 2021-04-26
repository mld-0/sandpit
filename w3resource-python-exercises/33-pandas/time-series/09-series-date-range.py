import pandas as pd

_dates = pd.Series(pd.date_range('2020-12-01', periods=31, freq='D'))
print("dates:")
print(_dates)
print(_dates.max())
print(_dates.min())
print(_dates.idxmax())
print(_dates.idxmin())

