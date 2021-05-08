import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, YearLocator, HourLocator, DayLocator, AutoDateLocator, WeekdayLocator

_start_date = pd.to_datetime('2020-04-01')
_end_date = pd.to_datetime('2020-09-30')

_df = pd.read_csv('alphabet_stock_data.csv')
_df['Date'] = pd.to_datetime(_df['Date']).dt.date
_df = _df.set_index('Date')

_indices_df_plot = (_df.index >= _start_date) & (_df.index <= _end_date)
_df_plot = _df.loc[_indices_df_plot]

print("_df_plot:")
print(_df_plot)
print()

#plt.subplots(constrained_layout=True)

_plot_top = plt.subplot2grid((5,4), (0,0), rowspan=3, colspan=4)
_plot_top.plot(_df_plot.index, _df_plot['Close'])

plt.gca().set_axisbelow(True)
plt.gca().minorticks_on()

#_majorloc = WeekdayLocator(byweekday=(0))  # Use mondays as major grid interval
#plt.gca().xaxis.set_major_locator(_majorloc)
plt.grid(which='major')

_mloc = DayLocator()  # Use day as minor grid interval
plt.gca().xaxis.set_minor_locator(_mloc)
plt.grid(which='minor', linestyle=':', linewidth='0.5')
plt.title("Alphabet Inc. Closing price")

_plot_bottom = plt.subplot2grid((5,3), (3,0), rowspan=2, colspan=4)
_plot_bottom.bar(_df_plot.index, _df_plot['Volume'])

plt.gca().set_axisbelow(True)
plt.gca().minorticks_on()

#_majorloc = WeekdayLocator(byweekday=(0))
#plt.gca().xaxis.set_major_locator(_majorloc)
plt.grid(which='major')

_mloc = DayLocator()
plt.gca().xaxis.set_minor_locator(_mloc)
plt.grid(which='minor', linestyle=':', linewidth='0.5')
plt.title("Alphabet Inc. Trading Volume", y=-0.5)

plt.gcf().set_size_inches(12,8)
plt.ticklabel_format(axis='y', style='plain')  # Prevent use of scientific notation for y-axis values
plt.gcf().autofmt_xdate()

#plt.show()
plt.show(block=False)
plt.pause(5)
plt.close()

