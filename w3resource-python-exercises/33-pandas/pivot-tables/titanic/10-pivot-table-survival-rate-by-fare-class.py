import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

_fare_bins = pd.qcut(_df['fare'], 4)
_age_bins = pd.cut(_df['age'], [0, 10, 30, 60, 80])

print("_fare_bins:")
print(_fare_bins)
print()

print("_age_bins:")
print(_age_bins)
print()

result = pd.pivot_table(_df, values=['survived'], index=['sex', _age_bins], columns=[_fare_bins, 'class'], aggfunc=np.mean)
print("result:")
print(result)

