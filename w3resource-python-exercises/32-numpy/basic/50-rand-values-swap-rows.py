import numpy as np

values = np.arange(16).reshape(4,4)
print(values)

#   swap first and last rows
values[[0,-1], :] = values[[-1,0], :]
print(values)

