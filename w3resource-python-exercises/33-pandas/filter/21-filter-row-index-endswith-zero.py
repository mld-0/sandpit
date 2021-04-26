import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)

results = _alcohol_data[_alcohol_data.index % 10 == 0]
#   or
results = _alcohol_data.filter(regex='0$', axis=0)
print("results:")
print(results)
