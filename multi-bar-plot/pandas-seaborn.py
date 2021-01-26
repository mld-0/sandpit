import matplotlib.pyplot as plt
import datetime
import pandas as pd
import seaborn as sns

#   LINK: https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars

x = [
    datetime.datetime(2011, 1, 4, 0, 0),
    datetime.datetime(2011, 1, 5, 0, 0),
    datetime.datetime(2011, 1, 6, 0, 0)
]
y = [4, 9, 2]
z = [1, 2, 3]
k = [11, 12, 13]

df = pd.DataFrame(zip(x*3, ["y"]*3+["z"]*3+["k"]*3, y+z+k), columns=["time", "kind", "data"])
plt.figure(figsize=(10, 6))
sns.barplot(x="time", hue="kind", y="data", data=df)
plt.show()
