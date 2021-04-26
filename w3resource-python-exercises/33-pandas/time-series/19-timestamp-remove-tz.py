import pandas as pd

_date1 = pd.Timestamp('2019-01-01', tz='Europe/Berlin')
_date2 = pd.Timestamp('2019-01-01', tz='US/Pacific')
_date3 = pd.Timestamp('2019-01-01', tz='US/Eastern')

print("dates:")
print(_date1)
print(_date2)
print(_date3)
print()

print("remove timezones:")
print(_date1.tz_localize(None))
print(_date2.tz_localize(None))
print(_date3.tz_localize(None))

