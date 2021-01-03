#   VIM SETTINGS: {{{3
#   vim: set tabstop=4 modeline modelines=10 foldmethod=marker:
#   vim: set foldlevel=2 foldcolumn=3: 
#   }}}1
import datetime
import dateparser
import pandas
import pprint
#   {{{2

#   DateTime ranges using pandas.date_range
#   LINK: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html
#   About:
#   {{{
#   pandas.date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs)[source]
#       Of the four parameters start, end, periods, and freq, exactly three must be specified. If freq is omitted, the resulting DatetimeIndex will have periods linearly spaced elements between start and end (closed on both sides).
#   Parameters
#   startstr or datetime-like, optional
#       Left bound for generating dates.
#   endstr or datetime-like, optional
#       Right bound for generating dates.
#   periodsint, optional
#       Number of periods to generate.
#   freqstr or DateOffset, default ‘D’
#       Frequency strings can have multiples, e.g. ‘5H’. See here for a list of frequency aliases.
#   tzstr or tzinfo, optional
#       Time zone name for returning localized DatetimeIndex, for example ‘Asia/Hong_Kong’. By default, the resulting DatetimeIndex is timezone-naive.
#   normalizebool, default False
#       Normalize start/end dates to midnight before generating date range.
#   namestr, default None
#       Name of the resulting DatetimeIndex.
#   closed{None, ‘left’, ‘right’}, optional
#       Make the interval closed with respect to the given frequency to the ‘left’, ‘right’, or both sides (None, the default).
#   **kwargs
#       For compatibility. Has no effect on the result.
#   }}}
#   Examples:
#   {{{
#   (see above) link for results of each statement
#   Specify start and end, with the default daily frequency.
pandas.date_range(start='1/1/2018', end='1/08/2018')
#   Specify start and periods, the number of periods (days).
pandas.date_range(start='1/1/2018', periods=8)
#   Specify end and periods, the number of periods (days).
pandas.date_range(end='1/1/2018', periods=8)
#   Specify start, end, and periods; the frequency is generated automatically (linearly spaced).
pandas.date_range(start='2018-04-24', end='2018-04-27', periods=3)
#   (month end frequency).
pandas.date_range(start='1/1/2018', periods=5, freq='M')
#   Multiples are allowed
pandas.date_range(start='1/1/2018', periods=5, freq='3M')
#   freq can also be specified as an Offset object.
pandas.date_range(start='1/1/2018', periods=5, freq=pandas.offsets.MonthEnd(3))
#   Specify tz to set the timezone.
pandas.date_range(start='1/1/2018', periods=5, tz='Asia/Tokyo')
#   closed controls whether to include start and end that are on the boundary. The default includes boundary points on either end.
pandas.date_range(start='2017-01-01', end='2017-01-04', closed=None)
#   Use closed='left' to exclude end if it falls on the boundary.
pandas.date_range(start='2017-01-01', end='2017-01-04', closed='left')
#   Use closed='right' to exclude start if it falls on the boundary.
pandas.date_range(start='2017-01-01', end='2017-01-04', closed='right')
#   }}}
#   Offset aliases
#   {{{
#   LINK: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases
#   B			business day frequency
#   C			custom business day frequency
#   D			calendar day frequency
#   W			weekly frequency
#   M			month end frequency
#   SM			semi-month end frequency (15th and end of month)
#   BM			business month end frequency
#   CBM			custom business month end frequency
#   MS			month start frequency
#   SMS			semi-month start frequency (1st and 15th)
#   BMS			business month start frequency
#   CBMS		custom business month start frequency
#   Q			quarter end frequency
#   BQ			business quarter end frequency
#   QS			quarter start frequency
#   BQS			business quarter start frequency
#   A, Y		year end frequency
#   BA, BY		business year end frequency
#   AS, YS		year start frequency
#   BAS, BYS	business year start frequency
#   BH			business hour frequency
#   H			hourly frequency
#   T, min		minutely frequency
#   S			secondly frequency
#   L, ms		milliseconds
#   U, us		microseconds
#   N			nanoseconds
#   }}}

def DTRange_FromStartEndAndCount(arg_dt_start, arg_dt_end, arg_count):
    return pandas.date_range(start=arg_dt_start, end=arg_dt_end, periods=arg_count)

def DTRange_FromStartEndAndInterval(arg_dt_start, arg_dt_end, arg_interval):
    return pandas.date_range(start=arg_dt_start, end=arg_dt_end, freq=arg_interval)

def DayStartAndEndFromDate(arg_date):
    if not isinstance(arg_date, datetime.datetime):
        arg_date = dateparser.parse(arg_date)
    result_start = arg_date.replace(hour=0, minute=0, second=0, microsecond=0)
    result_end = arg_date.replace(hour=23, minute=59, second=59)
    return [ result_start, result_end ]

dt_start = "2020-01-01"
dt_end = "2021-01-01"

dt_startAndEnd = DayStartAndEndFromDate(dt_start)
pprint.pprint(dt_startAndEnd)

dt_range_count20 = DTRange_FromStartEndAndCount(dt_start, dt_end, 20)
pprint.pprint(dt_range_count20)

dt_range_daily = DTRange_FromStartEndAndInterval(dt_start, dt_end, 'D')
pprint.pprint(dt_range_daily)

dt_range_monthly = DTRange_FromStartEndAndInterval(dt_start, dt_end, 'MS')
pprint.pprint(dt_range_monthly)

dt_range_yearly = DTRange_FromStartEndAndInterval(dt_start, dt_end, 'YS')
pprint.pprint(dt_range_yearly)

#   print as pandas timestamp and as python datetime
for loop_dt in dt_range_yearly:
    print(loop_dt)
    print(type(loop_dt))
    print(loop_dt.to_pydatetime())
    print(type(loop_dt.to_pydatetime()))

dt_start = "2020-01-01T00:00:00AEST"
dt_end = "2020-01-01T23:59:59AEST"

dt_range_daily = DTRange_FromStartEndAndInterval(dt_start, dt_end, 'min')
pprint.pprint(dt_range_daily)


#   }}}1

