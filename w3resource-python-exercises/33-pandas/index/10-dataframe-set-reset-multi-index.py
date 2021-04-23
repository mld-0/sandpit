import pandas as pd

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    't_id': ['t1', 't2', 't3', 't4', 't5', 't6']})
print("values:")
print(values)
print("values.index:")
print(values.index)
print()

values = values.set_index(['t_id', 'school_code', 'class'])
print("set_index([['t_id', 'school_code', 'class']):")
print(values)
print("values.index:")
print(values.index)
print()

values = values.reset_index(level=['t_id', 'class'])
#   or
#values = values.reset_index(level=[0,2])
print("reset_index(level=['t_id', 'class']):")
print(values)
print("values.index:")
print(values.index)

