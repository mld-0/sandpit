import pandas as pd

_data = pd.DataFrame({ "year": [2002, 2003, 2015, 2018], "day_of_the_year": [250, 365, 1, 140] })
print("_data:")
print(_data)
print()

_data['datetime'] = pd.to_datetime(_data['year'].astype(str) + "," + _data['day_of_the_year'].astype(str), format="%Y,%j")
print("_data convert to datetime:")
print(_data)

