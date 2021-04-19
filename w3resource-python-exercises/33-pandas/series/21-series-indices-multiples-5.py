import numpy as np
import pandas as pd

_n = 5
print("_n:")
print(_n)

values = pd.Series(np.arange(1,21))
print("values:")
print(values)
print()

#   Using boolean indexing
_indices_div_n = values % _n == 0
print("_indices_div_n:")
print(_indices_div_n.to_numpy())
result = values[_indices_div_n]
print("result:")
print(result)
print()

#   or

#   Result using indices array
result_indices = np.where(values.to_numpy() % _n == 0)[0]
#   or
result_indices = np.asarray(values % _n == 0).nonzero()[0]
print("result_indices:")
print(result_indices)
result = values[result_indices]
print("result:")
print(values[result_indices])


