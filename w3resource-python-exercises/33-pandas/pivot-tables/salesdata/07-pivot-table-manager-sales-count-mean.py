import numpy as np
import pandas as pd

_df = pd.read_excel('SaleData.xlsx')
print("_df:")
print(_df)
print()

result = _df.groupby(['Manager']).agg({'Sale_amt': [len, np.mean]}).swaplevel(axis=1)
#   or
result = pd.pivot_table(_df, index=['Manager'], values=['Sale_amt'], aggfunc=[len, np.mean])
print("result:")
print(result)

