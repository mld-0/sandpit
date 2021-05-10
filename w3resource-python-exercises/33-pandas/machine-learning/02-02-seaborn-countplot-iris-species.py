import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_iris = pd.read_csv('iris.csv')

ax = plt.subplots(1,1, figsize=(10,8))
sns.countplot(x='species', data=df_iris)

plt.title("Iris Species Count")

plt.show(block=False)
plt.pause(3)
plt.close()

