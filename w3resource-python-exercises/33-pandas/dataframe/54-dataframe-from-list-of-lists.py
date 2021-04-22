import numpy as np
import pandas as pd

_list_values = [[2,4], [1,3]]
_list_cols = ['col1', 'col2']

print("_list_values:")
print(_list_values)
print("_list_cols:")
print(_list_cols)

values = pd.DataFrame(_list_values, columns=_list_cols)
print("values:")
print(type(values))
print(values)

