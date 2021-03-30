import numpy as np

values = np.arange(16).reshape(4,4)
print(values)

values_new = values[::-1, ::-1]
print(values_new)
