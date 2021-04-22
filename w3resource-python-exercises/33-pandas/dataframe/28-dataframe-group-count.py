import numpy as np
import pandas as pd

values = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
print("values:")
print(values)
print()

_groupby_city = values.groupby('city')
print("_groupby_city groups:")
print(type(_groupby_city.groups))
print(_groupby_city.groups)
print()

_groupby_city_describe = _groupby_city.describe()
print("_groupby_city_describe:")
print(_groupby_city_describe)
print()

print("_groupby_city iterate:")
for loop_name, loop_group in _groupby_city:
    print(loop_name)
    print(loop_group)
    #print(_groupby_city.get_group(loop_name))
print()

_groupby_city_size = _groupby_city.size()
print("_groupby_city_size:")
print(type(_groupby_city_size))
print(_groupby_city_size)
print()

result = _groupby_city_size.reset_index(name='number of people')
print("result:")
print(type(result))
print(result)

