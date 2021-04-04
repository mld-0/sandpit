import numpy as np

a = np.array([[2,5,2],[1,5,5]])
b = np.array([[5,3,4],[3,2,5]])
print(a)
print(b)

result = np.divide(np.add(a,b), 2)
#   or
result = (a + b) / 2
#   or
result = np.mean((a, b), axis=(0))
print(result)


