import numpy as np

values = np.arange(10, 22).reshape(3, 4)
print(values)

#   Iterate over array (flat)
for x in np.nditer(values):
    print(x)


