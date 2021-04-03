import numpy as np

values = np.arange(16).reshape(4,4)
print(values)

result = values[:, [0,3]]
print(result)
