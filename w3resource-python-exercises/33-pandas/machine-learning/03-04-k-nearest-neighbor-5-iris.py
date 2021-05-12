import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

X = df_iris.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df_iris['species']

_test_percent = 0.3
print("_test_percent:")
print(_test_percent)
print()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=_test_percent)

print("train data:")
print(X_train.shape)
#print(X_train)
print()

print("test data:")
print(X_test.shape)
#print(X_test)
print()

_knn = KNeighborsClassifier(n_neighbors=5)
_knn.fit(X_train, y_train)

y_pred = _knn.predict(X_test)


_failed_test_indices = y_test[y_pred != y_test].index.to_list()
print("_failed_test_indices:")
print(_failed_test_indices)
print()

_success_rate = np.count_nonzero(y_test == y_pred) / y_pred.size
print("_success_rate:")
print(_success_rate)
print()

_failed_test_ans = y_pred[y_pred != y_test]
print("_failed_test_ans:")
print(_failed_test_ans)
print()

df_failed_tests = df_iris.iloc[_failed_test_indices, :].copy()
df_failed_tests['ans'] = _failed_test_ans
print("df_failed_tests:")
print(df_failed_tests)

