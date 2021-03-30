import numpy as np

x = np.arange(9).reshape(3,3)
print(x)

#   Iterate over columns
for i in range(x.shape[1]):
    print(x[:, i])
