import pandas as pd

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 37, 33, 30, 31, 32],
    'tcode': ['t1', 't2', 't3', 't4', 't5', 't6']})  

print("values:")
print(values)
print()

values = values.set_index(['tcode', 'school_code'])
print("set_index(['tcode', 'school_code'])")
print(values)
print()

#print(values.index.get_level_values('tcode'))

result = values.query("tcode == 't2'")
#   or
result = values[values.index.get_level_values('tcode') == 't2']
#   or
result = values[values.index.levels[values.index.names.index('tcode')] == 't2']
print("Select row(s) where tcode == 't2':")
print(result)
print()

result = values.query(("tcode == 't1'") and ("school_code == 's001'"))
#   or
result = values.query("(tcode == 't1') and (school_code == 's001')")
#   or
result = values[(values.index.get_level_values('tcode') == 't1') & (values.index.get_level_values('school_code') == 's001')]
print("Select row(s) where tcode == 't1' and school_code == 's001':")
print(result)

