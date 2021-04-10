import numpy as np

#values = np.random.uniform(1, 12, 5)
values = np.random.randint(0, 10, (5,5))
print(values)

v = 4

values_flat = np.array(values.flat)
_result_index = np.abs(values_flat- v).argmin()
_result_index_unraveled = np.unravel_index(_result_index, values.shape)
print(_result_index_unraveled)
print(_result_index)

result = values_flat[_result_index]
print(result)
