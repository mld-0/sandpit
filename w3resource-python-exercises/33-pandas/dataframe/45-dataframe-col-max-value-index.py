import numpy as np
import pandas as pd

_data = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_col = 'col1'
result_index = values[_col].argmax()
result = values.iloc[result_index, values.columns.get_loc(_col)]
print("%s max value/index" % _col)
print("%i at [%i]" % (result, result_index))

_col = 'col2'
result_index = values[_col].argmax()
result = values.iloc[result_index, values.columns.get_loc(_col)]
print("%s max value/index" % _col)
print("%i at [%i]" % (result, result_index))

_col = 'col3'
result_index = values[_col].argmax()
result = values.iloc[result_index, values.columns.get_loc(_col)]
print("%s max value/index" % _col)
print("%i at [%i]" % (result, result_index))

