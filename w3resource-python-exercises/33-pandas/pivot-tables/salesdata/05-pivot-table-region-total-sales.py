import numpy as np
import pandas as pd

_df = pd.read_excel('SaleData.xlsx')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, index=['Region'], aggfunc=np.sum)['Sale_amt']
#   or
result = pd.pivot_table(_df, index=['Region'], values=['Sale_amt'], aggfunc=np.sum)
#   or
result = _df.groupby(['Region']).agg({'Sale_amt': np.sum})
print("result:")
print(result)

