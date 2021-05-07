import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-04-30')

#   Rewrite - source of data, yfinance?
_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date'])
print("_df:")
print(_df)
print()

_df_plot = _df.loc[(_df['Date'] >= _start_date) & (_df['Date'] <= _end_date)]
#_df_plot = _df_plot.set_index('Date')

plt.figure(figsize=(6,6))
plt.suptitle('Trading Volume of Alphabet Inc.\n%s to %s' % (_start_date, _end_date))
plt.xlabel("Date", fontsize=12, color='black')
plt.ylabel("Volume", fontsize=12, color='black')

_df_plot['Volume'].plot(kind='bar')

plt.show(block=False)
plt.pause(3)
plt.close()

