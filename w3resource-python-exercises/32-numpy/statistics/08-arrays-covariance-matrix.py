import numpy as np

x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print(x)
print(y)

result = np.cov(x, y)
print(result)

