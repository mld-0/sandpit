import numpy as np
import pandas as pd

_df = pd.read_csv('iris.csv')
print("_df:")
print(type(_df))
print(_df)
print(_df.dtypes)
print()

print("shape:")
print(_df.shape)
print()

print("keys:")
print(_df.keys())
print()

print("info:")
print(_df.info())

