import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

results = _alcohol_data[(_alcohol_data['Year']==1986) & (_alcohol_data['WHO region']=='Western Pacific') & (_alcohol_data['Country']=='Viet Nam')]
print("results:")
print(results)

