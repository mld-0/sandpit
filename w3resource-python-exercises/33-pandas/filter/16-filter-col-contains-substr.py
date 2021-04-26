import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)

results = _alcohol_data[_alcohol_data['WHO region'].str.contains("Ea")]
print("results:")
print(results)

