import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date']).dt.date  # Disregard time component of datetime
print("_df:")
print(_df)
print(_df.dtypes)
print()

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-04-30')

_indices_df_plot = (_df['Date'] >= _start_date) & (_df['Date'] <= _end_date)

_df_plot = _df[['Open', 'Close', 'Date']].loc[_indices_df_plot]
_df_plot = _df_plot.set_index('Date')

print("_df_plot:")
print(_df_plot)
print()

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

print("fig:")
print(type(fig))
print(fig)
print()

print("ax:")
print(type(ax))
print(ax)
print()

plt.suptitle('Opening Closing price Alphabet Inc.\n%s to %s' % (_start_date, _end_date))

#   Use ax=ax to plot DataFrame within already created figure, instead of creating a new figure different to that we have labeled by default which is the behaviour (apparently) when plotting a DataFrame (but not an issue when plotting Series?)
#_df_plot.plot(kind='bar', ax=ax, stacked=True)
_df_plot.plot.barh(ax=ax, stacked=True)

ax.set_yticklabels([x.strftime("%Y-%m-%d") for x in _df_plot.index])  # Set (in this case) y-axis (not x) date label format (so that time is not included if index consists of datetimes instead of dates)

plt.show(block=False)  # Show plot for 3s and close
plt.pause(3)
plt.close()

