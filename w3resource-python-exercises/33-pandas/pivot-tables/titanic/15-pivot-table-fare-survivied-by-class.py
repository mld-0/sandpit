import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, index=['sex'], columns=['class'], aggfunc={'fare': np.mean, 'survived': np.mean})
print("result:")
print(result)
