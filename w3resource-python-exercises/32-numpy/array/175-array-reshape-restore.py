import numpy as np

values = np.arange(0, 40, 2)
print(values)

values = values.reshape(5,4)
print(values)

values = values.reshape(20)
#   or
values = values.flatten()
print(values)
