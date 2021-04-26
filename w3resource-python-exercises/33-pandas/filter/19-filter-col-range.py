import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

results = _alcohol_data[(_alcohol_data['Display Value'] < 2.5) & (_alcohol_data['Display Value'] > 0.5)]
#   or
results = _alcohol_data.query("`Display Value` < 2.5 & `Display Value` > 0.5")
print("results:")
print(results)


