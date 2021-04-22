import pandas as pd

_data = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_col_name = 'col2'
print("_col_name:")
print(_col_name)

_col_index = values.columns.get_loc(_col_name)
print("_col_index:")
print(_col_index)

