import pandas as pd

_data = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
values = pd.DataFrame(_data)
print("values:")
print(values)

_n = 3
print("_n:")
print(_n)

result = values.head(_n)
#   or
result = values.iloc[:3, :]

print("result:")
print(result)

