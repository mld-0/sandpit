import numpy as np

values = np.arange(10,110,10)
print(values)

#   Remove 1st, 4th, 5th elements
_indicies = [0, 3, 4]
values = np.delete(values, _indicies)
print(values)
