import numpy as np

_date_start_str = "2021-03"
_date_end_str = np.datetime64(_date_start_str) + np.timedelta64(1, 'M')

print("Weekdays in [%s, %s)" % (_date_start_str, _date_end_str))

result = np.busday_count(_date_start_str, _date_end_str)
print(result)

