import numpy as np

a = np.array([[1,2,3],[4,3,1]])
print(a)

print("argmax index")
print(a.argmax())

max_i, max_j = np.unravel_index(a.argmax(), a.shape)
print("Unraveled index max value")
print(max_i, max_j)

