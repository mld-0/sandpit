import numpy as np

a = np.array([[0, 1], [2, 3]])
b = np.array([[4, 5], [0, 3]])
print(a)
print(b)

result = (a + b) / 2
#   or
result = np.mean(np.dstack((a, b)), axis=2)

print(result)
