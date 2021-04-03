import numpy as np

values = np.array([1,2,3, 2,4,6, 1,2,12, 0,-12,6])

result = np.mean(values.reshape(-1, 3), axis=1)

print(result)
