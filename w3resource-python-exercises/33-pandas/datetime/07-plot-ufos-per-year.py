import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)
print()

_df['Year'] = _df['Date_time'].dt.year

result = _df['Year'].value_counts().sort_index()
print("result:")
print(result)

#result.plot(x="Year")
#plt.show()
