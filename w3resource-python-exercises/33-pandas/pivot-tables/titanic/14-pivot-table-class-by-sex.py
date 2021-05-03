import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, values=['survived'], index=['sex'], columns=['class'], aggfunc='count', margins=True)
print("result:")
print(result)

