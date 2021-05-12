import os
import tempfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

_temp_dir = tempfile.mkdtemp()
print("_temp_dir:")
print(_temp_dir)
print()

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

_iris_species = df_iris['species'].unique()
print("_iris_species:")
print(_iris_species)
print()

_colors = ('red', 'green', 'blue')
_saved_figures_sepal = []
_saved_figures_petal = []

#   Create historam for sepal/petal data of each species, and save as image. 
#   This is (apparently) (see below) the simplest way to combine multiple jointplots in a single figure.
#   LINK: https://stackoverflow.com/questions/35042255/how-to-plot-multiple-seaborn-jointplot-in-subplot
for loop_i, (loop_species, loop_color) in enumerate(zip(_iris_species, _colors)):
    _saved_figures_sepal.append(os.path.join(_temp_dir, "jointplot.sepal." + str(loop_i) + ".png"))
    _saved_figures_petal.append(os.path.join(_temp_dir, "jointplot.petal." + str(loop_i) + ".png"))
    loop_query = 'species=="%s"' % loop_species
    df_plot = df_iris.query(loop_query).drop(['species'], axis=1)
    g = sns.jointplot(x='sepal_length', y='sepal_width', data=df_plot, color=loop_color).plot_joint(sns.kdeplot, zorder=0, n_levels=6, color=loop_color)
    g.savefig(_saved_figures_sepal[-1])
    plt.close()
    g = sns.jointplot(x='petal_length', y='petal_width', data=df_plot, color=loop_color).plot_joint(sns.kdeplot, zorder=0, n_levels=6, color=loop_color)
    g.savefig(_saved_figures_petal[-1])
    plt.close()

#   Load each jointplot-as-image created earlier, and combine into a single plot.
f, axarr = plt.subplots(2, len(_iris_species), figsize=(14, 10))
for loop_i, (loop_figure_sepal, loop_figure_petal) in enumerate(zip(_saved_figures_sepal, _saved_figures_petal)):
    axarr[0][loop_i].imshow(mpimg.imread(loop_figure_sepal))
    axarr[1][loop_i].imshow(mpimg.imread(loop_figure_petal))

# turn off x and y axis
[ax.set_axis_off() for ax in axarr.ravel()]

#   Create a label for each column of subplots
for ax, col in zip(axarr[0], _iris_species):
    ax.annotate(col, xy=(0.5,1), xytext=(0,5), 
                xycoords='axes fraction', textcoords='offset points',
                size='large', ha='center', va='baseline')

plt.suptitle("Joint plots for Feature width vs Length for each Iris Species")
plt.tight_layout()

#plt.show()
plt.show(block=False)
plt.pause(3)
plt.close()

