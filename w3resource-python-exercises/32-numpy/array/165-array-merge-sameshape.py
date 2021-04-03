import numpy as np

a = np.random.random((5, 5, 1))
b = np.random.random((5, 5, 1))
c = np.random.random((5, 5, 1))
print(a.shape)
print(a)
print(b)
print(c)

result = np.concatenate((a, b, c), axis=2)
print(result.shape)
print(result)

