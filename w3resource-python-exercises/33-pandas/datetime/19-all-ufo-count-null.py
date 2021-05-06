import numpy as np
import pandas as pd

_df = pd.read_csv('ufo.csv')

result = _df.isnull().sum()

print("result:")
print(result)
