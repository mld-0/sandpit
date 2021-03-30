import numpy as np

x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print("Data type of the array x is:",x.dtype)
print(x)

y = x.astype(float)
print("New Type: ",y.dtype)
print(y)
