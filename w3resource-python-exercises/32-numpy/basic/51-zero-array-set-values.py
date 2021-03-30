import numpy as np

values = np.zeros(5*6).reshape(5,6)
print(values)

values[[0,2,4], ::2] = 3
values[[1,3], ::2] = 7
#   or
values[::2, ::2] = 3
values[1::2, ::2] = 7

print(values)
