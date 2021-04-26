import pandas as pd

dateset1 = pd.date_range('2029-01-01 00:00:00', periods=20, freq='3h10min')
print("Time series with frequency 3h10min:")
print(dateset1)
print()

dateset2 = pd.date_range('2029-01-01 00:00:00', periods=20, freq='1D10min20U')
print("Time series with frequency 1 day 10 minutes and 20 microseconds:")
print(dateset2)

