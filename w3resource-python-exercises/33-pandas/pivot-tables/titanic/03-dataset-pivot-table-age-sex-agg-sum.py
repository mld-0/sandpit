import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, index=['age', 'sex'], aggfunc=np.sum)
print("result:")
print(result)

