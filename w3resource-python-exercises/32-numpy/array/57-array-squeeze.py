import numpy as np

x = np.zeros((3, 1, 4))
print(x.shape)
print(x)

y = np.squeeze(x)
print(y.shape)
print(y)
