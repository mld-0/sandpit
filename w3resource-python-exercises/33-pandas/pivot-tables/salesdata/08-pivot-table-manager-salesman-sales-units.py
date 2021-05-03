import numpy as np
import pandas as pd

_df = pd.read_excel('SaleData.xlsx')
print("_df:")
print(_df)
print()

#   margins: include totals for each column
result = pd.pivot_table(_df, index=['Manager', 'SalesMan'], values=['Units', 'Sale_amt'], aggfunc=[np.sum], margins=True)
print("result:")
print(result)

