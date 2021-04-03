import numpy as np

values = np.arange(20).reshape(4,5)
print(values)

result = values[(values > 6) & (values % 3 == 0)]
print(result)

