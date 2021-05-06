import numpy as np
import pandas as pd

_daterange = pd.date_range('2018-01-01', periods=3, freq='H')
print("_daterange:")
print(_daterange)
print()

_daterange = _daterange.tz_localize('UTC')
print("_daterange:")
print(_daterange)
print()

_daterange = _daterange.tz_convert('America/Los_Angeles')
print("_daterange:")
print(_daterange)
