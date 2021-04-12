import numpy as np

values = np.arange(7)
print("values")
print(values)

n = 3
print("n")
print(n)
result = np.power(values, n)
#   or
result = values ** n
print("result")
print(result)
print()

n = np.ones_like(values) * 2
print("n")
print(n)
result = np.power(values, n)
#   or
result = values ** n
print("result")
print(result)


