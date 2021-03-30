import numpy as np

values = np.arange(16, dtype='int').reshape(4,4)
print(values)

values_new = values[:, [3,2,1,0]]
print(values_new)
