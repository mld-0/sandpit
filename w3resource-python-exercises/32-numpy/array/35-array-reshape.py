import numpy as np
x = np.array([1, 2, 3, 4, 5, 6])
print("6 rows and 0 columns")
print(x.shape)

y = np.array([[1, 2, 3],[4, 5, 6],[7,8,9]])
print("(3, 3) -> 3 rows and 3 columns ")
print(y)

x = np.array([1,2,3,4,5,6,7,8,9])
print("Change array shape to (3, 3) -> 3 rows and 3 columns ")
x.shape = (3, 3)
print(x)
