import numpy as np
import pandas as pd

values = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print("values:")
print(values)

result = values.map(lambda x: pd.Timestamp(x))
#   or
result = pd.to_datetime(values)
print("result:")
print(type(result))
print(result)

