import numpy as np
import pandas as pd

_data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}

values = pd.DataFrame(_data)
print("values:")
print(values)

_rows_drop = [2,4]
print("_rows_drop:")
print(_rows_drop)

values = values.drop(_rows_drop)
#   or
#values.drop(_rows_drop, inplace=True)
print("drop:")
print(values)

