import numpy as np

x = np.array([1,2,3], dtype=np.float64)
print(x)

print("array size:")
print(x.size)

print("array bytes:")
print(x.nbytes)

print("element bytes:")
print(x.itemsize)
