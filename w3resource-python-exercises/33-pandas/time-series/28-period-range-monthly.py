import pandas as pd
import datetime
from datetime import datetime, date

sdt = datetime(2020, 1, 1)
edt = datetime(2020, 12, 31)

dateset = pd.period_range(sdt, edt, freq='M')

print("All monthly boundaries of a given year:")
print(dateset) 
print()

print("Start and end time for each period:")
for loop_date in dateset:
   print ("{0}: {1}, {2}".format(loop_date, loop_date.start_time, loop_date.end_time)) 
