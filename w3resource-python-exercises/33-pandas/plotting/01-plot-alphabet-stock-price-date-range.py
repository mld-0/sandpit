import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-09-30')

#   Rewrite - source of data, yfinance?
_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date'])
print("_df:")
print(_df)
print()

_df_plot = _df.loc[(_df['Date'] >= _start_date) & (_df['Date'] <= _end_date)]
_df_plot = _df_plot.set_index('Date')

print("_df_plot:")
print(_df_plot)

plt.suptitle('Stock price of Alphabet Inc.,\n%s to %s' % (_start_date, _end_date), fontsize=18, color='black')
plt.xlabel('Date', fontsize=16, color='black')
plt.ylabel('$ price', fontsize=16, color='black')

_df_plot['Close'].plot(color='green')

plt.show(block=False)
plt.pause(3)
plt.close()

