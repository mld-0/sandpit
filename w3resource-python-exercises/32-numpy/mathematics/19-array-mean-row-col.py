import numpy as np

values = np.array([[10,30],[20,60]])
print(values)

result_col = values.mean(axis=0)
print(result_col)

result_row = values.mean(axis=1)
print(result_row)

