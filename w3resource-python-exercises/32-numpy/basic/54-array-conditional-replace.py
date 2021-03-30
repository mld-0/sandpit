import numpy as np

values = np.array([[5.54, 3.38, 7.99], [3.54, 8.32, 6.99], [1.54, 2.39, 9.29]])
print(values)
print()

print(np.where(values == 8.32, 18.32, values))
print()

print(np.where(values < 8.32, 18.32, values))
print()

print(np.where(values > 8.32, 18.32, values))


