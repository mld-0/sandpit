import numpy as np

values = np.random.randn(10, 4)
print(values)

#   Specify output printing precision
np.set_printoptions(precision=4)
print(values)

#   Round each element to a given number of decimals
result = np.round(values, decimals=4)
print(result)

