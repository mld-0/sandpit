import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

_index_duplicated = _alcohol_data['WHO region'].duplicated(keep='first')
print("_index_duplicated:")
print(_index_duplicated)
print()

_duplicated_values = _alcohol_data[_index_duplicated]
print("_duplicated_values:")
print(_duplicated_values)
print()

result = _alcohol_data[~_index_duplicated]
#   or
result = _alcohol_data.drop_duplicates('WHO region', keep='first')
print("result.shape:", result.shape)
print("result:")
print(result)

