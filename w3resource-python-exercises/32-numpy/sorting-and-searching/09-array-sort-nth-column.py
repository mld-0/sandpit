import numpy as np

#values = np.random.randint(0,10,(3,3))
values = np.array([[1,5,0],[3,2,5],[8,7,6]])
print("values")
print(values)

n = 1
print("n")
print(n)

_indices = values[:, n].argsort()
print("indices")
print(_indices)

result = values[_indices]
print("result")
print(result)

