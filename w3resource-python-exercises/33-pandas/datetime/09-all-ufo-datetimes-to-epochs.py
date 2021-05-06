import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')
_df['Date_time'] = _df['Date_time'].str.replace('24:', '00:')
_df['Date_time'] = pd.to_datetime(_df['Date_time'], format='%m/%d/%Y %H:%M')
print("_df:")
print(_df)
print()

result = _df['Date_time'].apply(lambda x: x.timestamp())
#   or
result = _df['Date_time'].values.astype(np.int64) // (10 ** 9)
print("result:")
print(result)

