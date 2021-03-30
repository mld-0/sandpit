import numpy as np

iterable = (x for x in range(10))
print(iterable)

print(np.fromiter(iterable, int))
