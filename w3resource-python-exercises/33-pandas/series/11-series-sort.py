import pandas as pd

a = pd.Series(['100', '200', 'python', '300.12', '400'])
print(a)
a_sorted = a.sort_values()
print(a_sorted)

b = pd.Series([2, 6, 1, 4, 3]) 
print(b)
b_sorted = b.sort_values()
print(b_sorted)

