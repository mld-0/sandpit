import pandas as pd

print("Subtract two timestamps of same time zone:")
date1 = pd.Timestamp('2019-03-01 12:00', tz='US/Eastern')
date2 = pd.Timestamp('2019-04-01 07:00', tz='US/Eastern')
print("Difference: ", (date2-date1))
print()

print("Subtract two timestamps of different time zone:")
date1 = pd.Timestamp('2019-03-01 12:00', tz='US/Eastern')
date2 = pd.Timestamp('2019-03-01 07:00', tz='US/Pacific')
# Remove the time zone and do the subtraction
print("Difference: ", (date1.tz_localize(None) - date2.tz_localize(None)))

