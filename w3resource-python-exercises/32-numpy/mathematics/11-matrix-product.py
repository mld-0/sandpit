import numpy as np
x = np.random.random((5,3))
print("First array:")
print(x.shape)
print(x)

y = np.random.random((3,2))
print("Second array:")
print(y.shape)
print(y)

z = np.dot(x, y)
print("Dot product of two arrays:")
print(z.shape)
print(z)
