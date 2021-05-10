import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

_iris_species = df_iris['species'].unique()
print("_iris_species:")
print(_iris_species)
print()

#   TODO: 2021-05-10T21:39:29AEST (this) produces 3 rows of 4 columns -> 1 row for each species, how to instead produce a column for each species, that is 4 rows of 3 columns, or the 'transpose' the subplots produced here. 

fig, axs = plt.subplots(3,4, figsize=(14,10))

title_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for loop_i, loop_species in enumerate(_iris_species):
    loop_query = 'species=="%s"' % loop_species
    df_plot = df_iris.query(loop_query).drop(['species'], axis=1)
    df_plot.hist(edgecolor='black', linewidth=1, ax=axs[loop_i], bins=10)

#   Remove title for each subplot - use values in title_cols instead, once per column
for ax in axs.flatten():
    ax.set_title('')

#   Create a label for each column of subplots
for ax, col in zip(axs[0], title_cols):
    ax.annotate(col, xy=(0.5,1), xytext=(0,5), 
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')

#   Create a label for each row of subplots
for ax, row in zip(axs[:,0], _iris_species):
    ax.annotate(row, xy=(0,0.5), xytext=(-ax.yaxis.labelpad - 5, 0),
                xycoords=ax.yaxis.label, textcoords='offset points', 
                size='large', ha='right', va='center')

plt.suptitle("Distribution of Iris Properties for each Species")

#plt.show()
plt.show(block=False)
plt.pause(3)
plt.close()

