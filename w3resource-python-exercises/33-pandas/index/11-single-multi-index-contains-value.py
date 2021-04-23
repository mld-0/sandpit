import pandas as pd

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]},
     index =  ['t1', 't2', 't3', 't4', 't5', 't6'])
print("values:")
print(values)
print()

_check_index = 't1'
print("_check_index:", _check_index)
result = _check_index in values.index
print("result:", result)

_check_index = 'a1'
print("_check_index:", _check_index)
result = _check_index in values.index
print("result:", result)
print()

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    't_id': ['t1', 't2', 't3', 't4', 't5', 't6']})

values = values.set_index(['t_id', 'school_code', 'class'])
print("values, update index:")
print(values)

_check_index = 't4'
print("_check_index:", _check_index)
result = _check_index in values.index
print("multiindex contains _check_index, result:", result)
result_level = [_check_index in x for x in values.index.levels]
print("multiindex level contains _check_index, result_level:")
print(result_level)

