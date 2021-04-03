import numpy as np

x = np.arange(16).reshape(4,4)
print(x)

slice_indices = tuple([[0,1,2], [0,1,3]])
print(slice_indices)

result = x[slice_indices]
print(result)
