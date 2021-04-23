import pandas as pd

values = pd.Series([1, 3, 5, 6, 9, 11, 13, 15], index=[0, 1, 2, 3, 4, 5, 7, 8])
print("values:")
print(values)
print()

_item = 11
print("_item:", _item)
print()

result_index = values[values == _item].index.to_list()
print("index(s) where values == _item:")
print(result_index)

