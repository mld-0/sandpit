import numpy as np

x = np.ones((2,3,4,5))
print(x.shape)
print(x)

print(np.rollaxis(x, 3, 1).shape)
print(np.rollaxis(x, 3, 1))
