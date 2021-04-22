import pandas as pd 

_data = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_col_except = 'col3'
print("_col_except:")
print(_col_except)

result = values.loc[:, values.columns != _col_except]
print("result:")
print(result)

