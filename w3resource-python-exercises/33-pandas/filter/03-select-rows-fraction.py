import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

result = _alcohol_data.sample(5)
print("random 5 rows:")
print(result)
print()

result = _alcohol_data.sample(frac=0.02)
print("random 2% of rows:")
print(result)

