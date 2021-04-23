import pandas as pd

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index =  [1, 2, 3, 4, 5, 6])
print("values:")
print(values)
print()

date_of_birth = ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997']

_idx = 3

values.insert(loc=_idx, column='date_of_birth', value=date_of_birth)
print("Insert column date_of_birth at _idx=%i" % _idx)
print(values)

