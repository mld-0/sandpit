import pandas as pd

_index = pd.DatetimeIndex(['2011-09-02', '2012-08-04',
                          '2015-09-03', '2010-08-04',
                          '2015-03-03', '2011-08-04',
                          '2015-04-03', '2012-08-04'])

_dates = pd.Series([0, 1, 2, 3, 4, 5, 6, 7], index=_index)

print("_dates:")
print(_dates)
print()

print("_dates['2015']:")
print(_dates['2015'])  # time-series indexed by year
#   or
#print(_dates.loc['2015'])  # time-series indexed by year
print()

print("_dates.index.is_monotonic:")
print(_dates.index.is_monotonic)  # is_monotonic - is datetime series sorted, either ascending or descending
print()

print("_dates['2012-01-01':'2012-12-31']")
print(_dates.sort_index().loc['2012-01-01':'2012-12-31'])  # indexing by slice is deprecated on non-monotonic time series (so sort it)

