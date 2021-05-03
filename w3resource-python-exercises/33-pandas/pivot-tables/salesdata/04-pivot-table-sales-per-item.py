import numpy as np
import pandas as pd

_df = pd.read_excel('SaleData.xlsx')
print("_df:")
print(_df)
print()

result = _df.groupby('Item').agg({'Units': np.sum})
#   or
result = pd.pivot_table(_df, index=['Item'], values=['Units'], aggfunc=np.sum)
print("result:")
print(result)

