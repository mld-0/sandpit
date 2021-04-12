import numpy as np

x = np.array([1, 4, 0], float)
y = np.array([2, 2, 1], float)
print("Matrices and vectors.")
print("x:")
print(x.shape)
print(x)
print("y:")
print(y.shape)
print(y)

print("Inner product of x and y:")
result = np.inner(x, y)
print(result.shape)
print(result)

print("Outer product of x and y:")
result = np.outer(x, y)
print(result.shape)
print(result)

print("Cross product of x and y:")
result = np.cross(x, y)
print(result.shape)
print(result)

