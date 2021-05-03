import numpy as np
import pandas as pd

df_vals = pd.read_excel('SaleData.xlsx')
print("df_vals:")
print(df_vals)
print()

result = df_vals.groupby(['Region', 'Manager', 'SalesMan']).agg({'Sale_amt': np.sum})
print("result: groupby(['Region', 'Manager', 'SalesMan']).agg({'Sale_amt': np.sum})")
print(result)
print()

result = pd.pivot_table(df_vals, index=['Region', 'Manager', 'SalesMan'], values=['Sale_amt'], aggfunc=np.sum)
print("result: pivot_table(df_vals, index=['Region', 'Manager', 'SalesMan'], values=['Sale_amt'], aggfunc=np.sum)")
print(result)

