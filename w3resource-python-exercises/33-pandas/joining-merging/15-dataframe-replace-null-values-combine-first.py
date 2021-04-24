import pandas as pd

df1 = pd.DataFrame({'A': [None, 0, None], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})

print("df1:")
print(df1)
print("df2:")
print(df2)
print()

result = df1.combine_first(df2)
print("result combine_first:")
print(result)

