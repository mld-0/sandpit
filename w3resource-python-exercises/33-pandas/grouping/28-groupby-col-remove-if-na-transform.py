import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'weight': [173, 192, 186, 167, 151, 159],
    'height': [35, None, 33, 30, None, 32]},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("values:")
print(values)
print()

result = values[~values['height'].isna().groupby(values['school_code']).transform('any')]
print("result:")
print(result)

