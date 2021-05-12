import numpy as np
import pandas as pd

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

X = df_iris.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
y = df_iris['species'].values

print("X (attributes):")
print(X)
print()

print("y (labels):")
print(y)


