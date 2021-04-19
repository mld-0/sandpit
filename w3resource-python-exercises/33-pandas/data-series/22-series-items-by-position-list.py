import numpy as np
import pandas as pd

values = pd.Series(np.arange(1,21))
print("values:")
print(values)

_indices = [0, 2, 6, 11, 16]
print("_indices:")
print(_indices)

result = values.take(_indices) 
print("result:")
print(result)

