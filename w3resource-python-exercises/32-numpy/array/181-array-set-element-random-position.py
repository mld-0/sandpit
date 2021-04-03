import numpy as np

n = 4
a = 10
i = 3

values = np.zeros(n*n).reshape(n,n)
print(values)

np.put(values, np.random.choice(range(n*n), i, replace=False), a)
print(values)

