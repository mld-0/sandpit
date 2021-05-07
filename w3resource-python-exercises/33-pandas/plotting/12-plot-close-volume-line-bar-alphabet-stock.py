import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-04-30')

_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date']).dt.date
_df = _df.set_index('Date')

_indices_df_plot = (_df.index >= _start_date) & (_df.index <= _end_date)
_df_plot = _df.loc[_indices_df_plot]

print("_df_plot:")
print(_df_plot)
print()

#fig = plt.figure(figsize=(12,8))
#_plot_top = fig.add_subplot(211)
#fig, ax = plt.subplots()
#fig.autofmt_xdate()

plt.subplots(constrained_layout=True)

_plot_top = plt.subplot2grid((5,4), (0,0), rowspan=3, colspan=4)
_plot_top.plot(_df_plot.index, _df_plot['Close'])

#   TODO: 2021-05-08T00:09:28AEST Set minor grid to have a given number of intervals between each major gridline

plt.gca().set_axisbelow(True)
plt.gca().minorticks_on()
#plt.gca().tick_params(which='major', length=1)
#plt.gca().tick_params(which='minor', length=(1/7))
plt.grid(which='major')
plt.grid(which='minor', linestyle=':', linewidth='0.5')

plt.title("Alphabet Inc. Closing price")

_plot_bottom = plt.subplot2grid((5,3), (4,0), rowspan=1, colspan=4)
_plot_bottom.bar(_df_plot.index, _df_plot['Volume'])

plt.gca().set_axisbelow(True)
plt.gca().minorticks_on()
#plt.gca().tick_params(which='major', length=1)
#plt.gca().tick_params(which='minor', length=(1/7))
plt.grid(which='major')
plt.grid(which='minor', linestyle=':', linewidth='0.5')


plt.title("Alphabet Inc. Trading Volume", y=1.2)

plt.gcf().set_size_inches(12,8)

#import matplotlib.ticker as ticker
#plt.gca().xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
#plt.gca().set_xticklabels(_df_plot.index, rotation=45)

plt.gcf().autofmt_xdate()

#plt.show()
plt.show(block=False)
plt.pause(3)
plt.close()

