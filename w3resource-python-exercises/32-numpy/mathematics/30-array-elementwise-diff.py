import numpy as np

values = np.array([1, 3, 5, 7, 0])
print(values)

result = np.ediff1d(values)
print(result)

result = np.hstack(([0, 0], result, [200]))
print(result)
