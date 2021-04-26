import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)

_rows = len(_alcohol_data.index)
_cols = len(_alcohol_data.columns)
#   or
_rows = _alcohol_data.shape[0]
_cols = _alcohol_data.shape[1]

print("rows:", _rows)
print("cols:", _cols)

