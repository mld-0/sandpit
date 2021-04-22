import numpy as np
import pandas as pd

_data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_index = 2
print("_index:")
print(_index)

#   Returns a Series with a single index value
result = values.iloc[_index]
print("result:")
print(type(result))
print(result)

#   Returns a DataFrame with a list index value
result = values.iloc[[_index]]
print("result:")
print(type(result))
print(result)

