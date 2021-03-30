import numpy as np

a = np.array([0, 10, 20, 40, 60])
b = np.array([0, 40])
print(a)
print(b)
print()

print(np.in1d(a, b))
print(a[np.in1d(a,b)])
print()

print(np.isin(a, b))
print(a[np.isin(a,b)])
