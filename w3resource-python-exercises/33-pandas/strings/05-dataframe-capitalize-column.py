import pandas as pd

values = pd.DataFrame({
    'name': ['alberto','gino','ryan', 'Eesha', 'syed'],
    'date_of_birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})

print("values:")
print(values)
print()

values['name'] = list(map(lambda x: x.capitalize(), values['name']))
#   or
values['name'] = values['name'].str.capitalize()

print(values)
