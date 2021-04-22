import pandas as pd

values = pd.DataFrame({ 'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'], 'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'], 'Age': [18.5, 21.2, 22.5, 22, 23] })

print("Original DataFrame:")
print(values)
print()

print("Global usage of memory of the DataFrame:")
print(values.info(memory_usage = "deep"))
print()

print("The usage of memory of every column of the said DataFrame:")
print(values.memory_usage(deep = True))

