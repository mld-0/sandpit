import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

X = df_iris.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
y = df_iris['species'].values

_test_percent = 0.3
print("_test_percent:")
print(_test_percent)
print()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=_test_percent)

print("train data:")
print(X_train.shape)
print(X_train)
print()

print("test data:")
print(X_test.shape)
print(X_test)

