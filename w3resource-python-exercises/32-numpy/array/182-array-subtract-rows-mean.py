import numpy as np

values = np.random.rand(3,5)
print(values)

values_row_mean = values.mean(axis=1, keepdims=True)
print(values_row_mean)

result = values - values_row_mean
print(result)

