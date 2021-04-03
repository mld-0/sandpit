import numpy as np

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])

z = np.vstack((x,y))
print(z)
#   or
z = np.stack((x,y), axis=0)
print(z)

