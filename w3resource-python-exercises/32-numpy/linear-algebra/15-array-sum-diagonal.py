import numpy as np

values = np.arange(6).reshape(2,3)
print(values)

result = np.trace(values)
#   or
result = np.sum(np.diag(values))

print(result)

