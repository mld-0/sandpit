import numpy as np
import pandas as pd

result = pd.date_range('2020-01-01', periods=12, freq='H')
print("Hourly frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='min')
print("Minute frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='S')
print("Second frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='2H')
print("2 Hour frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='5min')
print("5 Min frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='BQ')
print("Buisness Quarter frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='w')
print("Weekly (Sun) frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='w-MON')
print("Weekly (Mon) frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='2h20min')
print("2h20min frequency:")
print(result)
print()

result = pd.date_range('2020-01-01', periods=12, freq='1D10U')
print("1D10U frequency:")
print(result)

