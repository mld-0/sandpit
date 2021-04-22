import pandas as pd

_data = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
values = pd.DataFrame(data=_data)
print("values:")
print(values)

print("row 0:")
print(type(values.iloc[0]))
print(values.iloc[0])

print("row 3:")
print(type(values.iloc[3]))
print(values.iloc[3])

