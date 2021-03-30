import numpy as np

x = np.zeros((2, 3, 4))
print(x.shape)
print(x)

print(np.moveaxis(x, 0, -1).shape)
print(np.moveaxis(x, 0, -1))

print(np.moveaxis(x, -1, 0).shape)
print(np.moveaxis(x, -1, 0))

