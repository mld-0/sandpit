import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([2, 4, 6, 8, 10])
print("a:")
print(a)
print("b:")
print(b)

indices_a_notin_b = ~a.isin(b)
print("indices a notin b:")
print(indices_a_notin_b)

result = a[indices_a_notin_b]
print("result:")
print(result)

