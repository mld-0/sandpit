import datetime
from datetime import datetime, date

import pandas as pd
#from pandas.tseries.offsets import *

dt = datetime(2020, 1, 4)
print("Specified date:")
print(dt)
print()

print("One business day from the said date:")
obday = dt + pd.tseries.offsets.BusinessDay()
print(obday)
print()

print("Two business days from the said date:")
tbday = dt + 2 * pd.tseries.offsets.BusinessDay()
print(tbday)
print()

print("Three business days from the said date:")
thbday = dt + 3 * pd.tseries.offsets.BusinessDay()
print(thbday)
print()

print("Next business month end from the said date:")
nbday = dt + pd.tseries.offsets.BMonthEnd()
print(nbday)

