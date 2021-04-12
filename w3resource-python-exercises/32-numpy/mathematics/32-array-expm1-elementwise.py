import numpy as np

values = np.array([1, 2, 3, 4])
print(values)

result = np.expm1(values)
#   or
result = np.exp(values) - 1 
print(result)
