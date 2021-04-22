import numpy as np
import pandas as pd

_data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
values = pd.DataFrame(data=_data)
print("values:")
print(values)

#   New data as dict
_new_data = {'col1': 10, 'col2': 11, 'col3': 12}
print("_new_data:")
print(_new_data)
values = values.append(_new_data, ignore_index=True)
print("insert row:")
print(values)

#   New data as Series
_new_data = pd.Series([5, 7, 9], index=['col1', 'col2', 'col3'])
print("_new_data:")
print(_new_data)
values = values.append(_new_data, ignore_index=True)
print("insert row:")
print(values)

#   New data as list
_new_data = [3, 6, 9]
print("_new_data:")
print(_new_data)
values = values.append(pd.Series(_new_data, index=values.columns), ignore_index=True)
print("insert row:")
print(values)

