import numpy as np
import pandas as pd

sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))

sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])
print("sales_index:")
print(sales_index)

values = pd.Series(np.random.randint(1, 10, 8), index=sales_index)
print("values:")
print(values)

