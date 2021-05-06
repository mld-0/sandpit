import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

_df = pd.read_csv('ufo.csv')

_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)
print()

_df['ufo_year'] = _df['Date_time'].dt.year

years_data = _df['ufo_year'].value_counts()
years_index = years_data.index
years_values = years_data.values

print("years_data:")
print(type(years_data))
print(years_data)
print()

print("years_index:")
print(type(years_index))
print(years_index)
print()

print("years_values:")
print(type(years_values))
print(years_values)

plt.figure(figsize=(15,8))
plt.xticks(rotation=60)
plt.title("UFO sightings by year")
plt.xlabel("Year")
plt.ylabel("Number of reports")

years_plot = sns.barplot(x=years_index, y=years_values, palette='Reds')
#plt.show()

