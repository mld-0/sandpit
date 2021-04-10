import numpy as np

values = np.random.random((3,3))
print(values)

_max, _min = values.max(), values.min()

result = (values - _min) / (_max - _min)
print(result)

