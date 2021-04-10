import numpy as np

values = np.random.randint(0, 10, 10)
print("values")
print(values)

n = 4
print("n")
print(n)

_indices = np.argpartition(values, range(n))
print("indices")
print(_indices)

result = values[_indices]
print("result")
print(result)

