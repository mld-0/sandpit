import numpy as np

values = np.linspace(0, 1, 12)[1:-1]
#   or
values = np.linspace(0, 1, 11, endpoint=False)[1:]
print(values)


