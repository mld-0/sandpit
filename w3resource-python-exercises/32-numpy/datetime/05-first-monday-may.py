import numpy as np

_date_str = "2021-05"
_day_str = 'Mon'
print("First %s in %s" % (_day_str, _date_str))
result = np.busday_offset(_date_str, 0, roll='forward', weekmask=_day_str)
print(result)

_day_str = 'Sun'
print("First %s in %s" % (_day_str, _date_str))
result = np.busday_offset(_date_str, 0, roll='forward', weekmask=_day_str)
print(result)

