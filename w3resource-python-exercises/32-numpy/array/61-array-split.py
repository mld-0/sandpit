import numpy as np

x = np.arange(1, 15)
print("Original array:",x)

print("Split [2,6]")
print(np.split(x, [2, 6]))  # split into x[:2], x[2:6], x[6:]
print()

print(x[:2])
print(x[2:6])
print(x[6:])


