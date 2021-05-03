import numpy as np
import pandas as pd

values = pd.read_excel('SaleData.xlsx')
print("values:")
print(type(values))
print(values)
print()

result = values.groupby(['Region', 'Manager']).agg({'Sale_amt': np.sum})
#   or
result = pd.pivot_table(values, index=['Region', 'Manager'], values=['Sale_amt'], aggfunc=np.sum)
print("result:")
print(type(result))
print(result)


