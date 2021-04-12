import numpy as np

values = np.array([[1,2,3],[4,5,6]])
print("values")
print(values)

result = np.cumprod(values)
print("cumprod")
print(result)

result = np.cumprod(values, axis=0)
print("cumprod axis=0")
print(result)

result = np.cumprod(values, axis=1)
print("cumprod axis=1")
print(result)

