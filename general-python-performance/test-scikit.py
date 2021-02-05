from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix
from datetime import datetime

import pandas as pd

time_start = datetime.now()

# Dataset
iris = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')
time_load = datetime.now()
print(f'Dataset loaded, runtime = {(time_load - time_start).seconds} seconds')

# Train/Test split
X = iris.drop('species', axis=1)
y = iris['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
time_split = datetime.now()
print(f'Train/test split, runtime = {(time_split - time_start).seconds} seconds')

# Hyperparameter tuning
model = DecisionTreeClassifier()
params = {
    'criterion': ['gini', 'entropy'],
    'splitter': ['best', 'random'],
    'max_depth': [1, 5, 10, 50, 100, 250, 500, 1000],
    'min_samples_split': [2, 5, 10, 15, 20],
    'min_samples_leaf': [1, 2, 3, 4, 5],
    'max_features': ['auto', 'sqrt', 'log2']
}
clf = GridSearchCV(
    estimator=model, 
    param_grid=params, 
    cv=5
)
clf.fit(X_train, y_train)
time_optim = datetime.now()
print(f'Hyperparameter optimization, runtime = {(time_optim - time_start).seconds} seconds')

best_model = DecisionTreeClassifier(**clf.best_params_)
best_model.fit(X_train, y_train)

time_end = datetime.now()
print()
print(f'TOTAL RUNTIME = {(time_end - time_start).seconds} seconds')
