import numpy as np

values = np.array([[1,2,3],[4,5,6]])
print("values")
print(values)

result = np.cumsum(values)
print("cumsum")
print(result)

result = np.cumsum(values, axis=0)
print("cumsum axis=0")
print(result)

result = np.cumsum(values, axis=1)
print("cumsum axis=1")
print(result)

