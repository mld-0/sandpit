import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data.columns)
print()

_alcohol_data.columns = ['year','who_region','country','beverage_types','display_values']
print("rename columns:")
print(_alcohol_data.columns)
print()

_alcohol_data.rename(columns = {"who_region":"WHO_region","display_values":"Display_Value" },inplace = True)
print("rename some columns:")
print(_alcohol_data.columns)

