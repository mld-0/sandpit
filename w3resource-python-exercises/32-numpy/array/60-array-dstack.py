import numpy as np

a = np.array([[10],[20],[30]])
b = np.array([[40],[50],[60]])
print(a.shape)
print(a)
c = np.dstack((a, b))
print(c.shape)
print(c)
print()

a = np.array([10,20,30])
b = np.array([40,50,60])
print(a.shape)
print(a)
c = np.dstack((a, b))
print(c.shape)
print(c)

