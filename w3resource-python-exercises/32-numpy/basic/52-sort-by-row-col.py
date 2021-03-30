import numpy as np

values = np.array([[5.54, 3.38, 7.99], [3.54, 4.38, 6.99], [1.54, 2.39, 9.29]])
print(values)
print()

#   sort rows of each column
print(np.sort(values, axis=0))
print()

#   sort columns of each row
print(np.sort(values, axis=1))


