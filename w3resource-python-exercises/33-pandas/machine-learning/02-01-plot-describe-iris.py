import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris.csv')
print("df_iris:")
print(df_iris)
print()

#   Create plot and table of df_iris.describe() on the same figure, stacked vertically, with the plot 3 times the height of the table
fig, axs = plt.subplots(2,1, figsize=(12,6), gridspec_kw={'height_ratios': [3,1]})

plt.suptitle('Statistics of Iris Dataset')

#df_iris.describe().plot(kind='area', colormap="Accent", ax=axs[0])
df_iris.describe().plot(kind='bar', colormap="Accent", ax=axs[0])
axs[0].set_xlabel('Statistic')
axs[0].set_ylabel('Value')

axs[1].axis('off')
the_table = axs[1].table(
    cellText=df_iris.describe().to_numpy().T, 
    colLabels=df_iris.describe().index, 
    rowLabels=df_iris.describe().columns, 
    loc='center')

plt.show(block=False)
plt.pause(3)
plt.close()
