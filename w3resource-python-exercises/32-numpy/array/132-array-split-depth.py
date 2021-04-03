import numpy as np

x = np.arange(16).reshape(2, 2, 4)
print(x)
print("=" * 20)

a, b = np.dsplit(x, 2)
print(a)
print(b)
print("=" * 20)

a, b = np.split(x, 2, axis=2)
print(a)
print(b)
