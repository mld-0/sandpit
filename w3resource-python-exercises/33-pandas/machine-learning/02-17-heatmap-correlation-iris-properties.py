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
fig, axs = plt.subplots(1, 3, figsize=(16,10))

_plot_cmap = sns.diverging_palette(220, 10, as_cmap=True)

for loop_i, loop_species in enumerate(_iris_species):
    #print("loop_species: %s" % loop_species)
    #print()
    df_plot = df_iris.query('species == "%s"' % loop_species)
    df_plot_corr = df_plot.corr()
    #print("df_plot_corr:")
    #print(df_plot_corr)
    #print()
    sns.heatmap(df_plot_corr, linewidths=0.5, cmap=_plot_cmap, ax=axs[loop_i])
    axs[loop_i].title.set_text(loop_species)

plt.suptitle("Heatmap for Iris property correlation for each species")

plt.show(block=False)
plt.pause(3)
plt.close()

