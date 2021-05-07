import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-04-30')

_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date']).dt.date
_df = _df.set_index('Date')

_indices_df_plot = (_df.index >= _start_date) & (_df.index <= _end_date)
_df_plot = _df.loc[_indices_df_plot, ['Open', 'Close', 'High', 'Low']]

print("_df_plot:")
print(_df_plot)
print()

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

plt.suptitle("Histogram, Open/Close/High/Low for Alphabet Inc.\n%s to %s" % (_start_date.date(), _end_date.date()))

_df_plot.plot.hist(alpha=0.35, ax=ax)

plt.show(block=False)
plt.pause(3)
plt.close()

