import numpy as np


def array_contains_zero(x):
    #   Test that none of the elements of the array is zero
    print(not np.all(x))
    #   or (a test applicable to numbers besides 0)
    print(np.any(x[:] == 0))
    #   or
    print(0 in x[:])

x = np.array([1, 2, 3, 4])
array_contains_zero(x)
print()

x = np.array([0, 1, 2, 3])
array_contains_zero(x)



