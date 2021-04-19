import numpy as np
import pandas as pd
import datetime
import dateutil

_year = dateutil.parser.parse('2020-01-01')
print("_year:")
print(_year)

_year_end = _year + dateutil.relativedelta.relativedelta(years=1)
print("_year_end:")
print(_year_end)

result = pd.date_range(_year, periods=52, freq='W-SUN')
#   or
result = pd.date_range(start=_year, end=_year_end, freq='W-SUN', closed='left')
print("result:")
print(result)

