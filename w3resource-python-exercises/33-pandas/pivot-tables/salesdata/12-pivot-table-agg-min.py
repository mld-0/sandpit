import numpy as np
import pandas as pd

_df = pd.read_excel('SaleData.xlsx')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, index=['Item'], values=['Sale_amt'], aggfunc=np.min)
print("result:")
print(result)

