import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

result = _df.groupby('sex')[['survived']].mean()
#   or
result = pd.pivot_table(_df, index=['sex'], values=['survived'], aggfunc=np.mean)
print("result:")
print(result)
