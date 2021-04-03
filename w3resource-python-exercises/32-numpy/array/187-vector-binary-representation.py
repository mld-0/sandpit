import numpy as np

values = np.array([0,1,3,5,7,9,11,13,15])
print(values)

#   flatten values
print(values[:,None])

#   array [128, 64, 32, 16, 8, 4, 2, 1]
print(2**np.arange(8)[::-1])

#   binary values using bitwise comparison of values with 2**n array, converted from True/False to 1/0 (int)
values_bin = ((values[:,None] & (2**np.arange(8)[::-1])) != 0).astype(int)
print(values_bin)

