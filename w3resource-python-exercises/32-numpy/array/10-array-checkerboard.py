import numpy as np

values = np.zeros(8*8).reshape(8,8)
print(values)

values[::2, 1::2] = 1
values[1::2, ::2] = 1
print(values)
