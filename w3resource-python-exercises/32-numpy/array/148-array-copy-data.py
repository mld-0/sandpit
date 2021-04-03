import numpy as np

x = np.array([24, 27, 30, 29, 18, 14])
print(x)

y = np.empty_like(x)
y[:] = x
print(y)
#   or
y = np.copy(x)
print(y)
#   or
y = np.array(x, copy=True)
print(y)
