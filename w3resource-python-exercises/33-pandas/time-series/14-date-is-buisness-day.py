import pandas as pd

_days_series = pd.to_datetime(['2020-12-01', '2020-12-06', '2020-12-07', '2020-12-08'])
print("_days_series:")
print(_days_series)
print()

#   pd.bdate_range():
#       return fixed frequency DatetimeIndex, with buisness day as the default frequency

_is_buisnessday = lambda x: bool(len(pd.bdate_range(x, x)))

_check_is_buisnessday = _days_series.map(_is_buisnessday)
print("_check_is_buisnessday:")
print(_check_is_buisnessday)

