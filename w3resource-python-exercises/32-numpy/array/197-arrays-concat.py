import numpy as np

a = np.array([[4.5, 3.5], [5.1, 2.3]])
b = np.array([[1], [2]])
print(a.shape)
print(a)
print(b.shape)
print(b)

result = np.concatenate((a, b), axis=1)
#   or
result = np.hstack((a,b))

print(result.shape)
print(result)

