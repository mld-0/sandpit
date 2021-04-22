import numpy as np
import pandas as pd

_data = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
values = pd.DataFrame(_data)
print("values:")
print(values)
print()

_n = 3
print("_n:")
print(_n)
print()

result_col1 = values.nsmallest(_n, 'col1')
result_col2 = values.nsmallest(_n, 'col2')
result_col3 = values.nsmallest(_n, 'col3')

print("result_col1:")
print(result_col1)
print()

print("result_col2:")
print(result_col2)
print()

print("result_col3:")
print(result_col3)


