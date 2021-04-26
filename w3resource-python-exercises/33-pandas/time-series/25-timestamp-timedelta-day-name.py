import pandas as pd

newday = pd.Timestamp('2020-02-07')
print("First date:")
print(newday)
print(newday.day_name())
print()

print("Add 2 days with the said date:")
newday1 = newday + pd.Timedelta('2 day')
print(newday1)
print(newday1.day_name())
print()

print("Next business day:")
nbday = newday + pd.offsets.BDay()
print(nbday)
print(nbday.day_name())

