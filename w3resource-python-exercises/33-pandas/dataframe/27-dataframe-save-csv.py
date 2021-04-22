import tempfile
import numpy as np
import pandas as pd

_temp = tempfile.NamedTemporaryFile()
print("_temp:")
print(_temp)

_data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_delim = ','

#   Save DataFrame to csv
values.to_csv(_temp.name, sep=_delim, index=False)

#   Read and print csv
print("Read _temp:")
with open(_temp.name) as f:
    for loop_line in f:
        print(loop_line, end='')

#   Read csv to DataFrame
result = pd.read_csv(_temp.name, sep=_delim)
print("result:")
print(result)

