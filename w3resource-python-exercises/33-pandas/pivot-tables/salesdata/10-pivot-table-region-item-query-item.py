import numpy as np
import pandas as pd

_df = pd.read_excel('SaleData.xlsx')
print("_df:")
print(_df)
print()

result = pd.pivot_table(_df, index=['Region', 'Item'], values=['Units'])
print("result:")
print(result)
print()

result_query = result.query('Item == ["Television", "Home Theater"]')
print("result_query:")
print(result_query)
