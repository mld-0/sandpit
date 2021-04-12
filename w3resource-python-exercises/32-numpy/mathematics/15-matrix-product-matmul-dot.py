import numpy as np

x = [[1, 0], [1, 1]]
y = [[3, 1], [2, 2]]
print("x:")
print(x)
print("y:")
print(y)

print("matmul")
result = np.matmul(x,y)
print(result)

print("dot")
result = np.dot(x,y)
print(result)
