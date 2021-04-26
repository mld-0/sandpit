import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

results = _alcohol_data.query("`Display Value` > 2 & `Beverage Types` == 'Wine'")
print("results:")
print(results)


