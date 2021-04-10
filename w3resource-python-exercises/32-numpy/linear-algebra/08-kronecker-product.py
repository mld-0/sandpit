import numpy as np

a = np.array([1,2,3])
b = np.array([0,1,0])
print(a)
print(b)

result =  np.kron(a, b)
print(result)
print()

x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print(x)
print(y)

result = np.kron(x, y)
print(result)
