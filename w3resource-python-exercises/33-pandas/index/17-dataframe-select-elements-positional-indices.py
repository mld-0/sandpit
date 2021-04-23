import pandas as pd 
import numpy as np

sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'],
          ['city2', 'city1', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])

np.random.seed(1)

values = pd.DataFrame(np.random.randint(1,10,(8, 5)), index=sales_index)
print("values:")
print(values)
print()

result = values.take([1, 2, 5])
#   or
result = values.iloc[[1, 2, 5], :]
print("select rows [1, 2, 5]:")
print(result)
print()

result = values.take([1, 2], axis=1)
#   or
result = values.iloc[:, [1, 2]]
print("select columns [1, 2]:")
print(result)
print()

result = values.take([-1, -2], axis=1)
#   or
result = values.iloc[:, [-1, -2]]
print("select columns [-1, -2]:")
print(result)

