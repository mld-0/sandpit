import pandas as pd

a = pd.Series([2, 4, 6, 8, 10])
b = pd.Series([1, 3, 5, 7, 10])
print(a)
print(b)

result = a + b
print("add")
print(type(result))
print(result)

result = a - b
print("subtract")
print(type(result))
print(result)

result = a * b
print("multi")
print(type(result))
print(result)

result = a / b
print("divide")
print(type(result))
print(result)

