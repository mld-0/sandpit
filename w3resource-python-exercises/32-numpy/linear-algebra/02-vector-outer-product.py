import numpy as np

p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print(p)
print(q)

result = np.outer(p, q)
print(result)

