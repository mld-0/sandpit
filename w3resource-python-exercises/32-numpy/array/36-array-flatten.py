import numpy as np

x = np.array([[10, 20, 30], [20, 40, 50]])
print("Original array:")
print(x)
y = np.ravel(x)
print("New flattened array:")
print(y)

