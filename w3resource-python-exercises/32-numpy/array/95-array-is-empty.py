import numpy as np

x = np.arange(3*3).reshape(3,3)
y = np.array([])

# size 2, array is not empty
print(x.size)
print(x.size == 0)

# size 0, array is empty
print(y.size)
print(y.size == 0)
