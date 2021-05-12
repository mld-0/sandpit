import numpy as np
import pandas as pd
from sklearn import preprocessing

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

_iris_species = df_iris['species'].unique()
print("_iris_species:")
print(_iris_species)
print()

_le = preprocessing.LabelEncoder()
df_iris['species'] = _le.fit_transform(df_iris['species'])

_map_species = dict(zip(df_iris['species'].unique(), _iris_species))
print("_map_species:")
print(_map_species)
print()

print("df_iris:")
print(df_iris)
