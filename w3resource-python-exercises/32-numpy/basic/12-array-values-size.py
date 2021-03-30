import numpy as np

X = np.array([1, 7, 13, 105])

print("Original array:")
print(X)

print("Dimensions")
print(X.shape)

print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))
