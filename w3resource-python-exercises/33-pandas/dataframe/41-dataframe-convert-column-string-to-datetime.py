import pandas as pd
import numpy as np

#   Convert Series strings to datetimes
values = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])
print("values:")
print(values)
result = pd.to_datetime(values)
print(result)
print(result.dtypes)

#   Convert DataFrame column strings to datetimes
values = pd.DataFrame(['3/11/2000', '3/12/2000', '3/13/2000'])
print("values:")
print(values)
values[0] = pd.to_datetime(values[0])
#   or
print(values)
print(values.dtypes)

