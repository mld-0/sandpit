import numpy as np

#   Create 5,5,3 array
values = np.random.randint(0, 10, (5,5,3))
print(values.shape)
print(values)

#   Create 3,3,3 subarray
result = values[:3, :3, :]
print(result.shape)
print(result)

