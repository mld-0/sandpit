import numpy as np

x = np.array([1+2j,3+4j])
print("First array:")
print(x)

y = np.array([5+6j,7+8j])
print("Second array:")
print(y)

z = np.vdot(x, y)
print("vdot Product of above two arrays:")
print(z)

z = np.dot(x, y)
print("dot Product of above two arrays:")
print(z)
print()

x = np.array([[1+2j,3+4j], [1+1j, 2+2j]])
print("First array:")
print(x)

y = np.array([[5+6j,7+8j], [2+1j, 1+2j]])
print("Second array:")
print(y)

z = np.vdot(x, y)
print("vdot Product of above two arrays:")
print(z)

z = np.dot(x, y)
print("dot Product of above two arrays:")
print(z)





