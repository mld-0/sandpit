import numpy as np

a = np.array([[0, 1, 3], [5, 7, 9]])
b = np.array([[0, 2, 4], [6, 8, 10]])

c = np.concatenate((a, b), 0)
print(c.shape)
print(c)

c = np.concatenate((a, b), 1)
print(c.shape)
print(c)
