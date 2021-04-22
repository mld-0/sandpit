import pandas as pd

values = pd.DataFrame({ 'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'], 'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'], 'Age': [18.5, 21.2, 22.5, 22, 23] })

print("values:")
print(values)

values.columns = values.columns.str.lower().str.rstrip()
print("rename columns:")
print(values)

