import numpy as np
import pandas as pd

_data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
values = pd.DataFrame(_data)
print("values:")
print(values)

values_col2_list = values['col2'].to_list()
print("values_col2_list:")
print(type(values_col2_list))
print(values_col2_list)

