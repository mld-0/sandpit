import numpy as np    

x = np.arange(16.0).reshape(4, 4)
print(x)

a, b = np.vsplit(x, 2)
print(a)
print(b)
#   or
a, b = np.split(x, 2, axis=0)
print(a)
print(b)
