import numpy as np

x = 12.0
print(np.atleast_1d(x))
print()

x = np.arange(6.0).reshape(2, 3)
print(np.atleast_1d(x))
print()

print(np.atleast_1d(1, [3, 4]))
