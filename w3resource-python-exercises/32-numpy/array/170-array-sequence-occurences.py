import numpy as np

values = np.array([[1,2,3],[2,1,2]], np.int32)
print(values)

result = str(values).count("1 2")
print(result)
#   or
result = repr(values).count("1, 2")
print(result)

