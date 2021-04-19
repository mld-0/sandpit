import numpy as np
import pandas as pd

values = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("values:")
print(values)

_neighboured_smaller_values = lambda x: [i for i in range(1, values.size-1) if values[i] > values[i-1] and values[i] > values[i+1]]
result_indices = _neighboured_smaller_values(values)
print("result_indices:")
print(result_indices)

#   or

_smaller_neighbours = lambda x: np.diff(np.sign(np.diff(x)))
_neighboured_smaller_values_alt = lambda x: list(np.where(_smaller_neighbours(x) == -2)[0] + 1)

result_smaller_neighbours = _smaller_neighbours(values)
print("result_smaller_neighbours:")
print(result_smaller_neighbours)

result_indices = _neighboured_smaller_values_alt(values)
print("result_indices:")
print(result_indices)

