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

_df_plot['moving_avg_30_days'] = _df_plot['Adj Close'].rolling(window=30).mean()
_df_plot['expodential_avg_30_days'] = _df_plot['Adj Close'].ewm(span=20).mean()

print("_df_plot:")
print(_df_plot)
print()

plt.plot(_df_plot['Adj Close'], color='black', label='Adj Close')
plt.plot(_df_plot['moving_avg_30_days'], color='red', label='30 day moving average')
plt.plot(_df_plot['expodential_avg_30_days'], color='green', label='30 day expodential average')

plt.title('Closing price of Alphabet Inc.\n%s to %s' % (_start_date.date, _end_date.date))

plt.grid(True)
plt.gcf().autofmt_xdate()
plt.legend(loc=2)

plt.show(block=False)
plt.pause(3)
plt.close()

