import numpy as np
import pandas as pd

a = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = pd.Series([1, 3, 5, 7, 10])
print("a:")
print(a)
print("b:")
print(b)

b_items_index_in_a = [pd.Index(a).get_loc(i) for i in b]
print("b_items_index_in_a:")
print(b_items_index_in_a)

