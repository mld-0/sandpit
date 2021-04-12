import numpy as np

a = np.array([[1, 2], [2, 1]])
b = np.array([[2, 4], [1, 2]])
print("a")
print(a)
print("b")
print(b)

result = a + b
#   or
result = np.add(a, b)
print("sum")
print(result)

result = a * b
#   or
result = np.multiply(a, b)
print("product")
print(result)

result = a / b
#   or
result = np.divide(a, b)
print("quotient")
print(result)

