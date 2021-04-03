import numpy as np

values = np.arange(16)
values.shape = (4,4)
print(values)

result = values[[1,3], [0,3]]
print(result)

