import pandas as pd
import numpy as np

_cols = [1, 2, 4]
print("_cols:")
print(_cols)
print()

values = pd.read_excel('coalpublic2013.xlsx', usecols=_cols, skiprows=3)
print("values:")
print(values)

print("values.columns:")
print(values.columns)

