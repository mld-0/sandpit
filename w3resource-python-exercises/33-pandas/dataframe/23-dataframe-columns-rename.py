import numpy as np
import pandas as pd

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
values = pd.DataFrame(data=data)

print("values:")
print(values)

values = values.rename(columns={'col1': 'Column1', 'col2': 'Column2', 'col3': 'Column3'})
#   or
values.columns = ['Column1', 'Column2', 'Column3']
print("rename columns:")
print(values)



