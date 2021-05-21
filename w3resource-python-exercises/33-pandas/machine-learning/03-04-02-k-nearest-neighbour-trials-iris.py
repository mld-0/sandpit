import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

X = df_iris.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df_iris['species']

trial_results = []

#   Perform multiple fittings, with varying neighbour count and test percentage
for i in range(0, 10):
    for _test_percent in [x/100 for x in range(5, 75, 5)]:
        for _n_neighbours in range(1, 10, 1):
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=_test_percent)
            _knn = KNeighborsClassifier(n_neighbors=_n_neighbours)
            _knn.fit(X_train, y_train)
            y_pred = _knn.predict(X_test)
            _failed_test_indices = y_test[y_pred != y_test].index.to_list()
            _success_rate = np.count_nonzero(y_test == y_pred) / y_pred.size
            _failed_test_ans = y_pred[y_pred != y_test]
            df_failed_tests = df_iris.iloc[_failed_test_indices, :].copy()
            df_failed_tests['ans'] = _failed_test_ans
            loop_trial = {'failures': len(_failed_test_ans), 'test_percent': _test_percent, 'n_neighbors': _n_neighbours, 'success_rate': _success_rate}
            trial_results.append(loop_trial)
            #print(loop_trial)

df_results = pd.DataFrame(trial_results)
print("df_results:")
print(df_results)
print()

#   Then group results by test_percent and n_neighbors and plot mean success rate for each
_results_by_percent = df_results.loc[:, ['test_percent', 'success_rate']].groupby('test_percent').agg('mean')
print("_results_by_percent:")
print(_results_by_percent)
print()

_results_by_neighbours = df_results.loc[:, ['n_neighbors', 'success_rate']].groupby('n_neighbors').agg('mean')
print("_results_by_neighbours:")
print(_results_by_neighbours)

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

_results_by_percent.plot(ax=axs[0])
_results_by_neighbours.plot(ax=axs[1])

plt.show(block=False)
plt.pause(5)
plt.close()

