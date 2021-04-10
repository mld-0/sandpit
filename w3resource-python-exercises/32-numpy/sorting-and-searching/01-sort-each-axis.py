import numpy as np

values = np.array([[10,40],[30,20]])
print(values)

result = np.sort(values, axis=0)
print("Sort first axis")
print(result)

result = np.sort(values, axis=-1)
print("Sort last axis")
print(result)

result = np.sort(values, axis=None)
print("Sort flattened array")
print(result)
