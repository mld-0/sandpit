import pandas as pd
import numpy as np

_data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
values = pd.DataFrame(data=_data)
print("values:")
print(values)

values = values[['col3', 'col2', 'col1']]
#   or
values = values.reindex(columns=['col3', 'col2', 'col1'])
print("Swap col3, col1")
print(values)
