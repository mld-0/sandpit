import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-04-30')

_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date']).dt.date
_df = _df.set_index('Date')

_indices_df_plot = (_df.index >= _start_date) & (_df.index <= _end_date)
_df_plot = _df.loc[_indices_df_plot, ['Open', 'Close', 'High', 'Low', 'Adj Close', 'Volume']]

print("_df_plot:")
print(_df_plot)
print()

_axes = _df_plot.plot(subplots=True, figsize=(8,8))

for loop_ax in _axes:
    loop_ax.grid(which='major')
    loop_ax.xaxis.set_minor_locator(DayLocator())
    loop_ax.grid(which='minor')

plt.gcf().autofmt_xdate()
plt.ticklabel_format(axis='y', style='plain')  # Prevent use of scientific notation for y-axis values

plt.legend(loc='best')
plt.suptitle('Open, High, Low, Close, Adj Close, and Volume for Alphabt Inc.\nFrom %s to %s' % (_start_date, _end_date))

#plt.show()
plt.show(block=False)
plt.pause(3)
plt.close()

