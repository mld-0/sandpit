import numpy as np

x = np.array([0, 1, 3])
y = np.array([2, 4, 5])
print(x)
print(y)

result = np.corrcoef(x, y)
print(result)

