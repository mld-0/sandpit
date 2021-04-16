import numpy as np

x = np.arange(5)
print(x)

weights = np.arange(1, 6)

result = (x*(weights/weights.sum())).sum()
#   or
result = np.average(x, weights=weights)
print(result)

