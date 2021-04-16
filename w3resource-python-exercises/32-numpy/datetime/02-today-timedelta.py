import numpy as np

yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print(type(yesterday))
print(yesterday)

today = np.datetime64('today', 'D')
print(type(today))
print(today)

tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print(type(tomorrow))
print(tomorrow)

