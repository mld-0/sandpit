import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris.csv')

print("df_iris:")
print(df_iris)
print()

fig, ax = plt.subplots(1,1, figsize=(10,8))

df_iris.query('species == "setosa"').plot(kind='scatter', x='petal_length', y='petal_width', color='orange', label='Setosa', ax=ax)
df_iris.query('species == "versicolor"').plot(kind='scatter', x='petal_length', y='petal_width', color='blue', label='Versicolor', ax=ax)
df_iris.query('species == "virginica"').plot(kind='scatter', x='petal_length', y='petal_width', color='green', label='Virginica', ax=ax)

plt.gca().legend(bbox_to_anchor=(0.995,0.005), loc='lower right')

plt.xlabel('Petal Length (Cm)')
plt.ylabel('Petal Width (Cm)')
plt.suptitle('Petal Length vs Width')

plt.show(block=False)
plt.pause(3)
plt.close()

