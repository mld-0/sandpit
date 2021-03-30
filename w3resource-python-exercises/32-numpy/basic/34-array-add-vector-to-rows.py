import numpy as np

m = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1, 1, 0])

print("matrix m, vector v")
print(m)
print(v)

print("Add v to each row")
result = m + v
#   or
result = m[:,:] + v
print(result)
