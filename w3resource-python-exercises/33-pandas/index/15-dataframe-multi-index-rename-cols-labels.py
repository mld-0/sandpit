import numpy as np
import pandas as pd

sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
sales_tuples = list(zip(*sales_arrays))
sales_index = pd.MultiIndex.from_tuples(sales_tuples, names=['sale', 'city'])

values = pd.DataFrame(np.random.randn(8, 5), index=sales_index)
print("values:")
print(values)
print()

values = values.rename(columns={0: "col1", 1: "col2", 2:"col3", 3:"col4", 4:"col5"})
print("rename columns")
print(values)
print()

values = values.rename(index={"sale2": "S2", "city2": "C2"})
print("Rename index labels")
print(values)

