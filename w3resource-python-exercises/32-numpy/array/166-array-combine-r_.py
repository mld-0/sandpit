import numpy as np

array1 = ['PHP','JS','C++']
array2 = ['Python','C#', 'NumPy'] 
print(array1)
print(array2)

#   np.r_[array, array]
#       row-wise merging
#       This is used to concatenate any number of array slices along row (first) axis. This is a simple way to create numpy arrays quickly and efficiently.

result = np.r_[array1[:-1], [array1[-1]+array2[0]], array2[1:]]
print(result)
#   or
result = np.hstack((array1[:-1], [array1[-1]+array2[0]], array2[1:]))
print(result)

