import pandas as pd

_alcohol_data = pd.read_csv('world_alcohol.csv')
print("_alcohol_data:")
print(_alcohol_data)
print()

results = _alcohol_data[((_alcohol_data['Year']==1985) | (_alcohol_data['Year']==1989)) & ((_alcohol_data['WHO region']=='Americas') | (_alcohol_data['WHO region']=='Europe'))]
#   or
results = _alcohol_data.query('(Year==1985 | Year==1989) & (`WHO region`=="Americas" | `WHO region`=="Europe")')
print("results:")
print(results)

