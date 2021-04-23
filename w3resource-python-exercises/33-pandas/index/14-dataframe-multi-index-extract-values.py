import pandas as pd 
import numpy as np

sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]

sales_tuples = list(zip(*sales_arrays))
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])

np.random.seed(1)

values = pd.DataFrame(np.random.randint(1,10, (8, 5)), index=sales_index)
print("values:")
print(values)
print()

#   Single row
result = values.loc[('sale2', 'city2')]
print("single row, result:")
print(type(result))
print(result)
print()

#   Multiple rows
result = values.loc['sale1']
print("multiple rows, result:")
print(type(result))
print(result)
print()

#   Single value
result = values.loc[('sale1', 'city2'), 1]
#   or
result = values[1].loc[('sale1', 'city2')]
print("single value, result:")
print(result)

