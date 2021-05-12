import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.colors
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from scipy.stats import gaussian_kde

#   Ongoing: 2021-05-11T03:51:34AEST Solution given by w3resource doesn't match example output, (how to produce example output) (see below)
#   LINK: https://www.w3resource.com/machine-learning/scikit-learn/iris/python-machine-learning-scikit-learn-iris-visualization-exercise-13.php

#df_iris = pd.read_csv('iris.csv')
#
#print("df_iris:")
#print(df_iris)
#print()
#
#_colors = ['r', 'b', 'g']
#_labels = df_iris['species'].unique()
#
##   How to create 4x4 grid of plots, with color coding of categories?
#scatter_matrix(df_iris.loc[:, ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']], figsize=(15,11), label=_labels)
#
#for loop_species, loop_color in zip(_labels, _colors):
#    df_plot = df_iris[df_iris['species'] == loop_species]
#    df_plot = df_plot.drop('species', axis=1)
##    plt.scatter(df_plot.loc[:, :], df_plot.loc[:, :], label=loop_species)
#
##plt.show()
#plt.show(block=False)
#plt.pause(3)
#plt.close()


#   Solution: 
#   LINK: https://stackoverflow.com/questions/22943894/class-labels-in-pandas-scattermatrix
def factor_scatter_matrix(df, category, palette=None):
    '''Create a scatter matrix of the variables in df, with differently colored points depending on the value of df[category].
            df: pandas.DataFrame containing the columns to be plotted, as well as category. (df_iris)
            category: The column indicating which group each row belongs to. (Species column)
            palette: A list of hex codes, at least as long as the number of groups.  If omitted, a predefined palette will be used, but it only includes 9 groups.'''
    #   Get categorical values as _category_values from df, then drop column
    if isinstance(category, str):
        factor_name = category  
        _category_values  = df[category]  
        df = df.drop(factor_name,axis=1)  

    _species_unique = list(set(_category_values))

    #   Default colors
    if palette is None:
        palette = ['#e41a1c', '#377eb8', '#4eae4b', '#994fa1', '#ff8101', '#fdfc33', '#a8572c', '#f482be', '#999999']

    #   Ensure we have enough colors for _species_unique
    if len(_species_unique) > len(palette):
        raise ValueError('''Too many groups for the number of colors provided.  We only have {} colors in the palette, but you have {} groups.'''.format(len(palette), len(_species_unique)))

    color_map = dict(zip(_species_unique,palette))
    _mapped_colors = _category_values.apply(lambda group: color_map[group])

    axarr = scatter_matrix(df, figsize=(12,10), marker='o', color=_mapped_colors, diagonal=None)

    #   Plot the diagonal - each attribute versus itself (gaussian_kde)
    for rc in range(len(df.columns)):
        for group in _species_unique:
            y = df[_category_values == group].iloc[rc]
            gkde = gaussian_kde(y)
            ind = np.linspace(y.min(), y.max(), 1000)
            axarr[rc][rc].plot(ind, gkde.evaluate(ind), c=color_map[group])

    return axarr, color_map, _species_unique


df_iris = pd.read_csv('iris.csv')
axarr, color_map, _legend_values = factor_scatter_matrix(df_iris, 'species')


#plt.gca().legend(_legend_values, loc='center right', bbox_to_anchor=(1.55, 0.5))
plt.suptitle('Scatter Matrix Separability plot for Iris Data')

#plt.show()
plt.show(block=False)
plt.pause(3)
plt.close()

#   A similar result may be achieved with:
sns.pairplot(df_iris, hue='species')

plt.show(block=False)
plt.pause(3)
plt.close()


