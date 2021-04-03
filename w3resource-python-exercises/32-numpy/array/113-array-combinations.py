import numpy as np
import itertools

x = np.array([1, 2, 3])
y = np.array([4, 5])
z = np.array([6, 7])

result = np.array(np.meshgrid(x, y, z)).T.reshape(-1,3)
print(type(result))
print(result.shape)
print(result)

#   or

result = np.array(list(itertools.product(x, y, z)))
print(type(result))
print(result.shape)
print(result)
