import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn import preprocessing

#   PCA - principal component analysis
#       Reduce dimensionality of data while minimising loss of information.
#       The process of computing the principal components of a dataset and using them to perform a change of basis on the data. 
#       That is, it is an orthogonal linear transformation of the data to a new coordinate system, such that the greatest variance by some scalar projection of the data comes to lie on the first coordinate (first principal component), the second greatest on the second coordinate, ect.
#       PCA uses singular value decomposition to find orthogonal, recombined principle components from the original features which can explain most of the variance in the original data with remarkably less memory

#   PCA Algorithm:
#       Calculate covariance matrix
#       Calcualte eignvectors and eigenvalues of covariance matrix
#       Sort eigenvectors according to eigenvalues, decending order
#       Choose first k eigenvectors to be the k new dimensions
#       Transformed data is given by transpose of feature vector multiplied by transpose of origional data, where the feature vector is the column matrix of the chosen eigenvectors


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

ax = Axes3D(fig, auto_add_to_figure=False, rect=[0, 0, .95, 1], elev=48, azim=134)
fig.add_axes(ax)

_pca = decomposition.PCA(n_components=3)
_pca.fit(X)
X = _pca.transform(X)

_species_codes = list(zip(_iris_species, _iris_species_codes))

#   Position label relative to the mean location for each species
for loop_species, loop_species_code in _species_codes:
    ax.text3D(X[y == loop_species_code, 0].mean(),
              X[y == loop_species_code, 1].mean() + 1.6,
              X[y == loop_species_code, 2].mean(),
              loop_species, 
              horizontalalignment='center',
              bbox=dict(alpha=0.5, edgecolor='w', facecolor='w')
              )

_scatter = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap='plasma', edgecolor='k', alpha=0.9)
_legend = ax.legend(_scatter.legend_elements()[0], _iris_species, loc='lower right')

plt.suptitle('PCA n=3 plot for Iris data')

plt.show(block=False)
plt.pause(3)
plt.close()

