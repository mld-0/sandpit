import numpy as np

x = np.arange(1, 100)

n = x[(x % 3 == 0) | (x % 5 == 0)]
print(n)

print(n.sum())
