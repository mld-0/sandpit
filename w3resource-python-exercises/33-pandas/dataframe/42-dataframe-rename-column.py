import numpy as np
import pandas as pd

_data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
values = pd.DataFrame(_data)
print("values:")
print(values)

values.rename(columns = {'col2':'Column2'}, inplace=True)
#   or
values.columns = ['col1', 'Column2', 'col3']
print("rename col2:")
print(values)

