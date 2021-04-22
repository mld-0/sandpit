import numpy as np
import pandas as pd

_data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
values = pd.DataFrame(data=_data)
print("values:")
print(values)

_n = 4 
print("_n:")
print(_n)

_indices = values['col1'] == _n
print("_indices")
print(_indices.to_list())

result = values[_indices]
print("result:")
print(result)

