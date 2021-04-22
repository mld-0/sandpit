import pandas as pd

values = pd.DataFrame({ 'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'], 'date_of_birth': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'], 'age': [18.5, 21.2, 22.5, 22, 23] })

print("values:")
print(values)
print(values.dtypes)

result_numeric = values.select_dtypes(include = 'number')
print("result_numeric:")
print(result_numeric)

result_string = values.select_dtypes(include = 'object')
print("result_string:")
print(result_string)

