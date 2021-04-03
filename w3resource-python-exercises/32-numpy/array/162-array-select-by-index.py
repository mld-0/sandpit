import numpy as np

#values = np.array([[3, 2, 2, 7, 7, 7, 0, 3,], [5, 8, 4, 2, 9, 9, 3, 9,], [6, 8, 2, 8, 5, 7, 8, 7,], [5, 2, 4, 0, 4, 9, 2, 5,]])
values = np.random.randint(0, 10, (3, 4, 8))
print(values.shape)
print(values)

#tidx = np.array([0, 2, 2, 2])
tidx = np.random.randint(0, 3, 4)
print(tidx)

#result = values[tidx, np.arange(len(tidx)), :]
result = values[tidx, np.arange(len(tidx))]
print(result.shape)
print(result)

