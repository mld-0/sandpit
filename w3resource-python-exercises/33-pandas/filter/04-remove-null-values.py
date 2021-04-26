import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

_missing_vals_index = _alcohol_data.isnull().any(axis=1)
_missing_vals = _alcohol_data[_missing_vals_index]
print("_missing_vals:")
print(_missing_vals)
print()

result = _alcohol_data.dropna()
print("result:")
print(result)
