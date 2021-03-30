import numpy as np

values = np.arange(2,14).reshape(4,3)
print(values)

values_triu = np.triu(values, -1)
print(values_triu)
