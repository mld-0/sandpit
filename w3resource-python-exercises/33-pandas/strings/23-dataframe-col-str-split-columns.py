import pandas as pd

values = pd.DataFrame({
    'name': ['Alberto  Franco','Gino Ann Mcneill','Ryan  Parkes', 'Eesha Artur Hinton', 'Syed  Wharton'],
    'date_of_birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [18.5, 21.2, 22.5, 22, 23]
})
print("values:")
print(values)

values[['first', 'middle', 'last']] = values['name'].str.split(" ", expand=True)
print("Split name->first/middle/last:")
print(values)

