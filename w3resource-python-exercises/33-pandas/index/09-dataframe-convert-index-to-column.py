import pandas as pd

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index = ['t1', 't2', 't3', 't4', 't5', 't6'])

print("Original DataFrame:")
print(values)
print()

#   reset_index() resets all levels by default. DataFrame values has only level 0
values.reset_index(level=0, inplace=True)
#   or
#values.reset_index(inplace=True)

print("Convert index of the said dataframe into a column:")
print(values)

