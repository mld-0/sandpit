import pandas as pd
import dateutil

values = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
print("values:")
print(values)

_day_of_month = 11
print("_day_of_month:")
print(_day_of_month)

result = values.map(lambda x: dateutil.parser.parse(str(_day_of_month) + x))
print("result:")
print(result)

