import numpy as np

values = np.arange(36).reshape(4,9)
print(values)

a = 10
print("a = %i" % a)

result = np.where(np.any(values > a, axis=1))
print(result)

