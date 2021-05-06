import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.cm as cm
import seaborn as sns

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)
print()

_top_years = _df['Date_time'].dt.year.value_counts().head(10)
print("_top_years:")
print(_top_years)
print()

_is_top_year = lambda x: x if x in _top_years.index else None

month_vs_year = pd.pivot_table(_df, columns=_df['Date_time'].dt.month, index=_df['Date_time'].dt.year.apply(_is_top_year), values='city', aggfunc='count')
month_vs_year.index = month_vs_year.index.astype(int)
month_vs_year.columns = month_vs_year.columns.astype(int)

print("month_vs_year:")
print(month_vs_year)

def heatmap_timewheel(table, cmap='coolwarm_r', vmin=None, vmax=None,inner_r=0.25, pie_args={}):
    n, m = table.shape

    vmin= table.min().min() if vmin is None else vmin
    vmax= table.max().max() if vmax is None else vmax

    centre_circle = plt.Circle((0,0), inner_r, edgecolor='black', facecolor='white', fill=True, linewidth=0.25)
    plt.gcf().gca().add_artist(centre_circle)
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    cmapper = cm.ScalarMappable(norm=norm, cmap=cmap)

    for i, (row_name, row) in enumerate(table.iterrows()):
        labels = None if i > 0 else table.columns
        wedges = plt.pie([1] * m, radius=inner_r + float(n-i)/n, colors=[cmapper.to_rgba(x) for x in row.values], labels=labels, startangle=90, counterclock=False, wedgeprops={'linewidth':-1}, **pie_args)
        plt.setp(wedges[0], edgecolor='grey', linewidth=1.5)
        wedges = plt.pie([1], radius=inner_r+float(n-i-1)/n, colors=['w'], labels=[row_name], startangle=-90, wedgeprops={'linewidth':0})
        plt.setp(wedges[0], edgecolor='grey', linewidth=1.5)

plt.figure(figsize=(8,8))
plt.title("Timewheel of Hour vs Year", y=1.08, fontsize=30)
#heatmap_timewheel(month_vs_year, vmin=-20, vmax=80, inner_r=0.2)
heatmap_timewheel(month_vs_year, inner_r=0.2)

plt.show(block=False)
plt.pause(3)
plt.close()

