import numpy as np

x = np.arange(24).reshape(6,4)
print(x)

x_T = x.T
#   or
x_T = np.transpose(x)
print(x_T)
