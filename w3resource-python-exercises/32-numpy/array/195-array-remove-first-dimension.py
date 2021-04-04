import numpy as np

values = np.array([[[1, 2, 3, 4], [0, 1, 3, 4], [5, 0, 3, 2]]])
print(values.shape)
print(values)

result = np.add.reduce(values, axis=0)
#   or
result = values.reshape(values.shape[1:])
#   or
result = np.squeeze(values, axis=0)
print(result.shape)
print(result)

