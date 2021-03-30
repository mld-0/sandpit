import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)

array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)

print("Unique values that are in only one (not both) of the input arrays:")
print(np.setxor1d(array1, array2))
