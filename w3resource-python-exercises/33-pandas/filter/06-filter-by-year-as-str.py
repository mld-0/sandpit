import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

print("year 1985:")
print(_alcohol_data[_alcohol_data['Year']==1985])
print()

print("year 1989:")
print(_alcohol_data[_alcohol_data['Year']==1989])

