import numpy as np

values = np.array([[5.54, 3.38, 7.99], [3.54, 4.38, 6.99], [1.54, 2.39, 9.29]])
print(values)
print()

print(values > 5)
print(values[values > 5])
print()

print(values < 6)
print(values[values < 6])
