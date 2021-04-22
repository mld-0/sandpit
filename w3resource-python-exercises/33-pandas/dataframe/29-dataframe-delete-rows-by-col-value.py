import numpy as np
import pandas as pd

_data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 5, 5, 8], 'col3': [7, 8, 9, 0, 1]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_n = 5
print("_n:")
print(_n)

#   Remove rows where 'col2' equals _n
result = values[values['col2'] != _n]
print("result:")
print(result)

