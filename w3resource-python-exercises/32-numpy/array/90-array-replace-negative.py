import numpy as np

values = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
print(values)

values[values < 0] = 0
print(values)
