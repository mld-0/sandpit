import pandas as pd


_date_range = pd.date_range('2020-01-01', periods=45)
print("_date_range:")
print(type(_date_range))
print(_date_range)

print("_date_range.size:")
print(_date_range.size)

