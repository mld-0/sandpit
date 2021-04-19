import numpy as np

a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])

print("Checking for complex number:")
print(np.iscomplex(a))

print("Checking for real number:")
print(np.isreal(a))

print("Checking for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))
