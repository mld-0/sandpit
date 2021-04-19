import pandas as pd

a = pd.Series([2, 4, 6, 8, 10])
b = pd.Series([1, 3, 5, 7, 10])
print(a)
print(b)

result = a == b
print("Equality")
print(type(result))
print(result)

result = a > b
print("Greater-than")
print(type(result))
print(result)

result = a < b
print("Less-than")
print(type(result))
print(result)

