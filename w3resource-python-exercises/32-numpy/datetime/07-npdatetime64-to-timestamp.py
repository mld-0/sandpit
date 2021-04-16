import numpy as np
import datetime

_dt_now = datetime.datetime.utcnow()
print(type(_dt_now))
print(_dt_now)

_dt_now_np = np.datetime64(_dt_now)
print(type(_dt_now_np))
print(_dt_now_np)

_dt_now_ts = (_dt_now_np - np.datetime64('1970-01-01T00:00:00')) / np.timedelta64(1, 's')
print(type(_dt_now_ts))
print(_dt_now_ts)
#   or
_dt_now_ts = _dt_now_np.astype('float') / 1000000
print(type(_dt_now_ts))
print(_dt_now_ts)

_dt_now = datetime.datetime.utcfromtimestamp(_dt_now_ts)
print(type(_dt_now))
print(_dt_now)

