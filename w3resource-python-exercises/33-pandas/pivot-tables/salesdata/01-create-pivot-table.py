import numpy as np
import pandas as pd

values = pd.read_excel('SaleData.xlsx')
print("values:")
print(type(values))
print(values)
print()

result = pd.pivot_table(values, index=['Region', 'SalesMan'])
print("result:")
print(type(result))
print(result)
print()

print("result.index:")
print(result.index)

