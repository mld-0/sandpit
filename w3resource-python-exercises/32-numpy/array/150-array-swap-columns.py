import numpy as np

values = np.arange(12).reshape(3,4)
print(values)

#   swap columns 0, 1
values[:, [0,1]] = values[:, [1,0]]
print(values)
