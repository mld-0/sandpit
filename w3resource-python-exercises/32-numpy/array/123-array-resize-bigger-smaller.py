import numpy as np

x = np.arange(16).reshape(4,4)

new_size = (2,2)
print(new_size)

y = np.resize(x, new_size)
print(y)
print()

new_size = (6,6)
print(new_size)

z = np.resize(x, new_size)
print(z)
