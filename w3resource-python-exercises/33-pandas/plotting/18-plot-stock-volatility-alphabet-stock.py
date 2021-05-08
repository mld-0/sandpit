import numpy as np
import pandas as pd
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

#   We define volatility as the standard deviation of the rolling percentage change
_df_volatility = _df_plot.pct_change(periods=1).rolling(window=30, min_periods=30).std()

print("_df_volatility:")
print(_df_volatility)

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

plt.suptitle("Volatility for Alphabet Inc.\n%s to %s" % (_start_date.date(), _end_date.date()))

_df_volatility.plot(ax=ax)
plt.grid(True)

plt.xlim([_df_volatility.index[0], _df_volatility.index[-1]])  # use entire date range as x-axis domain
plt.gcf().autofmt_xdate()


plt.show(block=False)
plt.pause(3)
plt.close()

