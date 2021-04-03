import numpy as np

values = np.array([1, 7, 8, 2, 0.1, 3, 15, 2.5])
print(values)

k = 4

result = np.sort(values)[:k]
#   or
result = values[np.argpartition(values, k)[:k]]

print(result)
