import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

_age_bins = pd.cut(_df['age'], [0, 20, 55])
print("_age_bins:")
print(_age_bins)
print()

result = pd.pivot_table(_df, values=['survived'], index=['sex', _age_bins], columns=['class'])
print("result:")
print(result)
