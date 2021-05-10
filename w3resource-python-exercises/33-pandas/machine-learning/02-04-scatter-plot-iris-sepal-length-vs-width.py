import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris.csv')

print("df_iris:")
print(df_iris)
print()

fig, ax = plt.subplots(1,1, figsize=(10,8))

df_iris.query('species == "setosa"').plot(kind='scatter', x='sepal_length', y='sepal_width', color='orange', label='Setosa', ax=ax)
df_iris.query('species == "versicolor"').plot(kind='scatter', x='sepal_length', y='sepal_width', color='blue', label='Versicolor', ax=ax)
df_iris.query('species == "virginica"').plot(kind='scatter', x='sepal_length', y='sepal_width', color='green', label='Virginica', ax=ax)

plt.xlabel('Sepal Length (Cm)')
plt.ylabel('Sepal Width (Cm)')
plt.suptitle('Sepal Length vs Width')

plt.show(block=False)
plt.pause(3)
plt.close()

