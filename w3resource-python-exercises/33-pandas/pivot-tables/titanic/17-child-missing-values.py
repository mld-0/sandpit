import numpy as np
import pandas as pd

_df = pd.read_csv('titanic.csv')
print("_df:")
print(_df)
print()

result = _df.loc[_df['who'] == 'child'].isnull().sum()
print("result:")
print(result)
