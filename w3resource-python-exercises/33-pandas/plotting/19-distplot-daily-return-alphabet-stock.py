import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-09-30')

_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date']).dt.date
_df = _df.set_index('Date')

_indices_df_plot = (_df.index >= _start_date) & (_df.index <= _end_date)
_df_plot = _df.loc[_indices_df_plot, ['Adj Close']]

print("_df_plot:")
print(_df_plot)
print()

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

_daily_change = _df_plot.pct_change(periods=1)

print("_daily_change:")
print(_daily_change)
print()

sns.histplot(_daily_change, bins=100, color='purple', ax=ax, kde=True)

plt.suptitle('Daily %% return of Alphabet Inc.\n%s to %s' % (_start_date.date(), _end_date.date()))
plt.grid(True)

plt.show(block=False)
plt.pause(3)
plt.close()

