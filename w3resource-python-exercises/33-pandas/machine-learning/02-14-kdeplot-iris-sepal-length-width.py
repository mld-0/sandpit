import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

_iris_species = df_iris['species'].unique()
print("_iris_species:")
print(_iris_species)
print()

df_plot = df_iris[df_iris['species'] == 'setosa']

sns.kdeplot(data=df_plot, x='sepal_length', y='sepal_width', cmap='plasma', shade=True)
plt.title('Iris Setosa Sepal length vs width')
plt.xlabel('Length (cm)')
plt.ylabel('Width (cm)')

#plt.show()
plt.show(block=False)
plt.pause(3)
plt.close()

