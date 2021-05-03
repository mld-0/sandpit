import numpy as np
import pandas as pd

_df = pd.read_excel('SaleData.xlsx')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, index=['Region', 'Item'], values=['Units'], aggfunc=np.sum)
#   or
result = _df.groupby(['Region', 'Item']).agg(np.sum)['Units']
#   or
result = _df.groupby(['Region', 'Item']).agg({'Units': np.sum})

print("result:")
print(result)
