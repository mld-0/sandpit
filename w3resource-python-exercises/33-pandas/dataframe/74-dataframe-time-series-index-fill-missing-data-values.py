import pandas as pd
import numpy as np

_data = {"c1":[120, 130 ,140, 150, np.nan, 170], "c2":[7, np.nan, 10, np.nan, 5.5, 16.5]}
values = pd.DataFrame(_data)
values.index = pd.date_range('2020-01-01', periods=6, freq='D')

print("values:")
print(values)

result = values.interpolate()
print("interpolate:")
print(result)

