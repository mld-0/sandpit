import numpy as np
import pandas as pd

_df = pd.read_excel('SaleData.xlsx')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, index=['Region', 'Manager', 'SalesMan'], values=['Sale_amt'])
print("result:")
print(result)
print()

result_query = result.query('Manager == ["Douglas"]')
print("result_query:")
print(result_query)
