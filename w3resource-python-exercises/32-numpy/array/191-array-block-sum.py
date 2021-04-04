import numpy as np

values = np.ones((9,12))
#values = np.arange(9*12).reshape(9,12)
print("values")
print(values)

k = 3
print("block step")
print(k)

_step_col = np.arange(0, values.shape[0], k)
print("step col")
print(_step_col)

_step_row = np.arange(0, values.shape[1], k)
print("step row")
print(_step_row)

block_col_sum  = np.add.reduceat(values, _step_col, axis=0)
print("block col sum")
print(block_col_sum)

result = np.add.reduceat(block_col_sum, _step_row, axis=1)
print("result")
print(result)

