import pandas as pd

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})

print("values:")
print(values)

values1 = values.set_index('t_id')
print("values1, t_id as index:")
print(values1)

values2 = values1.reset_index()
print("values2, reset index:")
print(values2)

