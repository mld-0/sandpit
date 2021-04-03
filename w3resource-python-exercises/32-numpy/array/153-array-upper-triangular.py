import numpy as np

values = np.arange(18).reshape(6,3)
print(values)

result = values[np.triu_indices(3)]
print(result)

result = values[np.triu_indices(2)]
print(result)

