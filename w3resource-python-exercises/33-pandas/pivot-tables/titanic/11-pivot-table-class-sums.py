import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, index=['sex', 'class'], values=['survived'], aggfunc='count')
result.columns = ['count']

print("result:")
print(result)

