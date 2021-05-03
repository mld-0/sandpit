import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, values=['survived'], index=['sex'], columns=['class'], margins=True)
print("result:")
print(result)
print("result.index:")
print(result.index)
print("result.columns:")
print(result.columns)

