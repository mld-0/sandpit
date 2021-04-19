import numpy as np
import pandas as pd

values = pd.Series([1, 3, 5, 8, 10, 11, 15])
print("values:")
print(values)


result = [ np.NaN ]
result += [values[i] - values[i-1] for i in range(1, values.size)]
#   or
result = values.diff()
print("result:")
print(result.to_numpy())

