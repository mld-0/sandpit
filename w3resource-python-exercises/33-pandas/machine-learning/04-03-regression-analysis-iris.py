import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

X = df_iris.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df_iris['species']

_test_percent = 0.2
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

#model = LogisticRegression(solver='lbfgs', multi_class='multinominal').fit(X_train, y_train)
model = LogisticRegression(solver='lbfgs', multi_class='multinomial', n_jobs=-1, max_iter=1000)#.fit(X, y)
print(type(model))
print(model)
model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = metrics.accuracy_score(prediction, y_test)

print("accuracy:")
print(accuracy)

