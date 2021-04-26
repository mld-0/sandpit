import pandas as pd
import numpy as np
import datetime

dates = [datetime.datetime(2011, 9, 1), datetime.datetime(2011, 9, 2)]
time_series = pd.Series(np.random.randn(2), dates)

print("time_series:")
print(type(time_series))
print(time_series)
print()

print("time_series.index:")
print(type(time_series.index))
print(time_series.index)

