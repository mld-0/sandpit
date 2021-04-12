import numpy as np

values = np.arange(-4, 5)
print(values)

result = values < 0
#   or
result = np.signbit(values)
print(result)

