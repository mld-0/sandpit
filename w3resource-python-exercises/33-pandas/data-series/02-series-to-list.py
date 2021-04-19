import pandas as pd

values = pd.Series([2, 4, 6, 8, 10])
print(type(values))
print(values)

values_list = values.tolist()
print(type(values_list))
print(values_list)

