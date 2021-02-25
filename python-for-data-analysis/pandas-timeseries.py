#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3:
#   }}}1
import numpy as np
import pandas as pd
#   {{{2
#   See: OReilly Python for Data Analysis Ch11

#   Python datetime basics
from datetime import datetime
from datetime import timedelta

#   current time as python datetime
now = datetime.now()
print(f"now=({now})")
print(f"{now.year}, {now.month}, {now.day}, {now.hour}, {now.minute}, {now.second}, {now.microsecond}")
print()

#   datetime delta
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
print(f"delta=({delta})")
print(f"{delta.days}, {delta.seconds} {delta.microseconds}")  # delta contains only days, seconds, and microseconds
print(f"{delta.total_seconds()}")

print(timedelta(3))  # days
print(timedelta(3, 12345))  # days, seconds
print(timedelta(3, 12345, 24))  # days, seconds, microseconds

var = datetime(2011, 1, 7) + timedelta(7, 3208)  # add 7 days, 53mins, 28sec to datetime
print(var)
print()

#   String <-> datetime conversions

#   datetime.strptime requires datetime format to be specified
var_str = '2011-01-03'
var_dt = datetime.strptime(var_str, '%Y-%m-%d')
print(var_dt)
print()

#   Using dateutil.parser.parse (included with pandas)
from dateutil.parser import parse
var_dt = parse(var_str)
print(var_dt)
var_dt = parse('Jan 31, 1997 10:45 PM')
print(var_dt)
var_dt = parse('6/12/2011', dayfirst=True)
print(var_dt)
print()

#   Using pd.to_datetime
var_datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
var_dts = pd.to_datetime(var_datestrs)
print(var_dts)
var_dts = pd.to_datetime(var_datestrs + [None])  # handle 'missing' values
print(var_dts)
print(pd.isnull(var_dts))
print()

#   Pandas Time-Series
var_dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
var_values = np.random.randn(len(var_dates))

var_ts = pd.Series(var_values, index=var_dates)
print(var_ts)
print(var_ts.index)  # index values represented as DatetimeIndex
print(var_ts.index.dtype)  # pandas stores timestamps using numpy's datetime64 datatype

var_dt = var_dts[0]
print(var_dt)  # scalar values from a DatetimeIndex are pandas Timestamp objects
print()

#   operations between differently indexed time series automatically align on dates
print(var_ts + var_ts[::2])
print()

#   Time series behaves like any other pandas.Series when indexing and selecting data based on label
stamp = var_ts.index[2]
print(var_ts[stamp])

#   One can also pass a string that is interpretable as a date
print(var_ts['1/10/2011'])  # Note the Americanized date 
print(var_ts['20110110'])  
print(var_ts[datetime(2011, 1, 7)])  # slicing can also be done by datetime object
print()

#   slice with timestamps not contained in a time series to perform a range query
print(var_ts['1/6/2011':'1/11/2011'])
print(var_ts['2011-01-06':'2011-01-11'])
print()

#   truncate()
#       slices a Series between two dates
print(var_ts.truncate(after='2011-09-01'))
print()

#   For longer time series, a year or only a year and month can be passed to easily select slices of data
longer_ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(longer_ts['2001'])
print()
print(longer_ts['2001-05'])
print()

#   These operations also apply to DataFrames
var_dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
var_values = np.random.randn(len(var_dates), 4)
var_longDF = pd.DataFrame(var_values, index=var_dates, columns=['Colorado', 'Texas', 'New York', 'Ohio'])
print(var_longDF.loc['2001-05'])
print()

#   Time Series with duplicate indices
#       indexing into this time series will now either produce scalar values or slices depending on whether a timestamp is duplicated
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000', '1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.arange(5), index=dates)
print(dup_ts)
print(dup_ts.is_unique)
grouped_dup_ts = dup_ts.groupby(level=0)  # groupby
print(grouped_dup_ts.mean())
print(grouped_dup_ts.count())
print()

#   Generic time series in pandas are assumed to be irregular; that is, they have no fixed frequency
#   Convert the sample time series to be fixed daily frequency by calling resample
print(var_ts.resample('D'))
print()


#   Generating Date Ranges
index = pd.date_range('2012-04-01', '2012-06-01')
index = pd.date_range(start='2012-04-01', periods=20)
index = pd.date_range(end='2012-06-01', periods=20)
index = pd.date_range('2000-01-01', '2000-12-01', freq='BM')  # BM = Buisness end-of-month
index = pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True)  # normalize to midnight

#   Frequencies and Date Offsets
index = pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4h')
index = pd.date_range('2000-01-01', periods=10, freq='1h30min')
#   or
_freq = pd.tseries.offsets.Hour(1) + pd.tseries.offsets.Minute(30)
index = pd.date_range('2000-01-01', periods=10, freq=_freq)

#   Week-of-month
rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')  # 3rd Friday of every month
print(rng)

#   Shifting (Leading and Lagging) data
ts = pd.Series(np.random.randn(4), index=pd.date_range('1/1/2000', periods=4, freq='M'))
#   Continue: 2021-02-25T22:14:51AEDT shifting data


#   Time Zone handling

#   Operations between timezones

#   Periods and period arithmetic


#   }}}1
