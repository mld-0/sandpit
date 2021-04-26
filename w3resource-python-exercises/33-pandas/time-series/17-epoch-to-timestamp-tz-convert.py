import pytz
import tzlocal
import pandas as pd

_epoch = 1621132355

#   Epoch to pandas timestamp
_datetime = pd.to_datetime(_epoch, unit='s')
print("_datetime:")
print(type(_datetime))
print(_datetime)
print("_datetime.tzinfo:")
print(_datetime.tzinfo)
print()

#   pandas timestamp, set timezone
_datetime_utc = _datetime.tz_localize('UTC')
print("_datetime_utc:")
print(type(_datetime_utc))
print(_datetime_utc)
print("_datetime_utc.tzinfo:")
print(type(_datetime_utc.tzinfo))
print(_datetime_utc.tzinfo)
print()

#   Convert pandas timestamp timezone
print("local timezone:")
print(_datetime.tz_localize('UTC').tz_convert(tzlocal.get_localzone()))
print("Europe/Berlin:")
print(_datetime.tz_localize('UTC').tz_convert('Europe/Berlin'))
print()

#   Pandas timestamp to python datetime
_datetime_py = _datetime.to_pydatetime()
print("_datetime_py:")
print(type(_datetime_py))
print(_datetime_py)
print("_datetime_py.tzinfo:")
print(_datetime_py.tzinfo)
print()

#   Python datetime set timezone
_datetime_py_utc = _datetime_py.replace(tzinfo=pytz.timezone('UTC'))
print("_datetime_py_utc:")
print(type(_datetime_py_utc))
print(_datetime_py_utc)
print("_datetime_py_utc.tzinfo:")
print(type(_datetime_py_utc.tzinfo))
print(_datetime_py_utc.tzinfo)
print()

