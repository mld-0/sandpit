import numpy as np
import pandas as pd

values = pd.DataFrame()
print("values:")
print(values)

_data = {'col1': range(3), 'col2': range(3)}
print("_data:")
print(_data)

values = values.append(pd.DataFrame(_data))
print("append data as DataFrame:")
print(values)

