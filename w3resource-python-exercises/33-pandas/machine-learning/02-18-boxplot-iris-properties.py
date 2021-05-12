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

#fig, axs = plt.subplots(311, figsize=(10,8))
fig, axs = plt.subplots(1, 3, figsize=(14,6))


#_plot_cmap = sns.diverging_palette(220, 10, as_cmap=True)

for loop_i, loop_species in enumerate(_iris_species):
    df_plot = df_iris.query('species == "%s"' % loop_species)
    axs[loop_i].title.set_text(loop_species)
    res = sns.boxplot(data=df_plot, width=0.5, fliersize=5, ax=axs[loop_i])
    res.set_xticklabels(res.get_xmajorticklabels(), fontsize = 8, rotation=0)

plt.suptitle("Boxplot for Iris property distribution for each species")
sns.set_context("paper", rc={"font.size":8,"axes.titlesize":8,"axes.labelsize":4}) 

#plt.show()
plt.show(block=False)
plt.pause(3)
plt.close()


