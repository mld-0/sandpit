import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

print("two rows:")
print(_alcohol_data.iloc[:2])

print("two columns:")
print(_alcohol_data.iloc[:, :2])

_result_cols = _alcohol_data[['Display Value', 'Year']]
#   or
_result_cols = _alcohol_data.loc[:, ['Display Value', 'Year']]
#   or
_result_cols = _alcohol_data.iloc[:, [_alcohol_data.columns.get_loc(x) for x in ['Display Value', 'Year']]]
print("specific columns ['Display Value', 'Year']:")
print(_result_cols)

