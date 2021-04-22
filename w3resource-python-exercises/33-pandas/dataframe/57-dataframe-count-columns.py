import pandas as pd

_data = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
values = pd.DataFrame(_data)
print("values:")
print(values)

result = len(values.columns)
#   or
result = values.shape[1]
print("Number of columns:")
print(result)
