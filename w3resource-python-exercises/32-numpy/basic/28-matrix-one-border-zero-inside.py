import numpy as np

values = np.ones((10, 10))

values[1:-1, 1:-1] = 0

print(values)
