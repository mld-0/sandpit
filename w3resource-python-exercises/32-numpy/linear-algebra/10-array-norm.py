import numpy as np

values = np.arange(7)
print(values)
result = np.linalg.norm(values)
print(result)
print()

values = np.matrix('1,2; 3,4')
print(values)
result = np.linalg.norm(values)
print(result)
print()

values = np.array([1,1])
print(values)
result = np.linalg.norm(values)
print(result)
