import numpy as np

a = np.array([1,2,5])
b = np.array([2,1,0])
print(a)
print(b)

result = np.inner(a,b)
print(result)
print()

x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print(x)
print(y)

result = np.inner(x,y)
print(result)

