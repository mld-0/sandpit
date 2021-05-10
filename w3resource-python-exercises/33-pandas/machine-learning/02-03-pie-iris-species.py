import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#   Plot label 'species' overlaps with label 'versicolor'

df_iris = pd.read_csv('iris.csv')

ax = plt.subplots(1,1, figsize=(10,8))

#   Function to create percentage labels that also include quantites
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

_iris_species_counts = df_iris['species'].value_counts()
_iris_species_counts.name = ""  # remove name, since otherwise it will be printed next to graph, overlapping one of our labels

_iris_species_counts.plot.pie(explode=[0.1,0.1,0.1], autopct=make_autopct(df_iris['species'].value_counts()), shadow=True, figsize=(10,8))

plt.title("Iris Species %")

plt.show(block=False)
plt.pause(3)
plt.close()

