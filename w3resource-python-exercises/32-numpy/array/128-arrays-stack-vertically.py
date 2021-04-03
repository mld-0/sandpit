import numpy as np

a = np.array([[0,1,2], [3,4,5], [6,7,8]])
b = np.array([[0,3,6], [9,12,15], [18,21,24]])
print(a)
print(b)

result = np.vstack((a, b))
print(result)
#   or
result = np.concatenate((a, b), axis=0)
print(result)
