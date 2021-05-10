import numpy as np
import pandas as pd

df_iris = pd.read_csv('iris.csv')

print("df_iris:")
print(df_iris)
print()

print(df_iris.describe())
print()

print(type(df_iris['species']))
print(df_iris['species'])
print()

result = df_iris.groupby(['species']).agg('count').iloc[:,0]
result.name = result.index.name
result.index.name = None
#   or
result = df_iris['species'].value_counts()
print("result:")
print(result)

