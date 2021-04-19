import numpy as np
import pandas as pd

values = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print("values:")
print(values)

_index_smallest = values.idxmin()
_index_largest = values.idxmax()

print("_index_smallest:")
print(_index_smallest)
print("_index_largest:")
print(_index_largest)

