import numpy as np
x = np.arange(24).reshape((2,3,4))
print("Array x:")
print(x.shape)
print(x)

print("Array y:")
y = np.arange(4)
print(y.shape)
print(y)

result = np.inner(x, y)
print("Inner of x and y arrays:")
print(result.shape)
print(result)

