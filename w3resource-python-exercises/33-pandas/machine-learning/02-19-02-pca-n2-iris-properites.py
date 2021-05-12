import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import preprocessing

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

_iris_species = df_iris['species'].unique()
print("_iris_species:")
print(_iris_species)
print()

#   Convert species labels into numbers
_le = preprocessing.LabelEncoder()
df_iris['species'] = _le.fit_transform(df_iris['species'])
_iris_species_codes = df_iris['species'].unique()

X = df_iris.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
y = df_iris['species'].values

fig = plt.figure(1, figsize=(8,6))
ax = fig.gca()

_pca = decomposition.PCA(n_components=2)
_pca.fit(X)
X = _pca.transform(X)

_species_codes = list(zip(_iris_species, _iris_species_codes))

_scatter = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='plasma', edgecolor='k', alpha=0.9)
_legend = ax.legend(_scatter.legend_elements()[0], _iris_species, loc='lower right')

plt.suptitle('PCA n=2 plot for Iris data')

plt.show(block=False)
plt.pause(3)
plt.close()

