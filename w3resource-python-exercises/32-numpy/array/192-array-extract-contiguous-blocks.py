import numpy as np

#values = np.random.randint(0,10,(12,12))
values = np.random.randint(0,10,(6,6))
values = np.array([[5, 5, 9, 7, 5, 5,], [1, 3, 8, 8, 0, 3,], [0, 3, 3, 9, 8, 1,], [9, 5, 0, 8, 7, 3,], [9, 1, 8, 5, 9, 5,], [8, 7, 3, 8, 4, 3,]])
print("values")
print(values)

n = 3
print("n")
print(n)

i = 1 + values.shape[0] - n
j = 1 + values.shape[1] - n
print("i, j")
print(i, j)

_strides = values.strides + values.strides
print("strides")
print(_strides)

#   np.lib.stride_tricks.as_strided
result = np.lib.stride_tricks.as_strided(values, shape=(i, j, n, n), strides = _strides)
print("result, as_strided")
print(result.shape)
print(type(result))
print(result)

#   np.lib.stride_tricks.sliding_window_view
result = np.lib.stride_tricks.sliding_window_view(values, window_shape=(n,n), axis=(0,1))
print("result, sliding_window_view")
print(result.shape)
print(type(result))
print(result)


