import numpy as np
x = np.arange(16).reshape((4, 4))
print("Original array:")
print(x)

print("Split [2,6]")
print(np.hsplit(x, [2, 6]))

print(x[:, :2])
print(x[:, 2:6])
print(x[:, 6:])
