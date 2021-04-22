import numpy as np
import pandas as pd

_data = {'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_new_col = [1, 2, 3, 4, 7]
print("_new_col:")
print(_new_col)

values.insert(0, column='col1', value=_new_col)
print("insert col1:")
print(values)

