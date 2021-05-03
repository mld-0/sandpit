import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

_brackets_age = [0, 10, 30, 60, 80]
print("_brackets_age:")
print(_brackets_age)
print()

result = pd.cut(_df['age'], _brackets_age)
print("result:")
print(result)

