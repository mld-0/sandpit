import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-09-30')

_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date']).dt.date
_df = _df.set_index('Date')

_indices_df_plot = (_df.index >= _start_date) & (_df.index <= _end_date)
_df_plot = _df.loc[_indices_df_plot, 'Adj Close']

_df_percentage_change = _df_plot.pct_change(periods=1)
#   or
_df_percentage_change = (_df_plot - _df_plot.shift(periods=1)) / _df_plot

print("_df_percentage_change:")
print(_df_percentage_change)
print()

_df_percentage_change.plot(figsize=(10,7), legend=True, linestyle='--', marker='o')

plt.suptitle('Daily %% return of Alphabet Inc.\n%s to %s' % (_start_date.date(), _end_date.date()))
plt.grid(True)

plt.show(block=False)
plt.pause(3)
plt.close()

