import pandas as pd

values = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
values = pd.to_datetime(values)
print("values:")
print(values)

result_dayofmonth = values.dt.day
print("result_dayofmonth:")
print(result_dayofmonth.to_list())

result_dayofyear = values.dt.dayofyear
print("result_dayofyear:")
print(result_dayofyear.to_list())

result_weekofyear = values.dt.isocalendar().week
print("result_weekofyear:")
print(result_weekofyear.to_list())

result_day = values.dt.day_name()
print("result_day:")
print(result_day.to_list())

