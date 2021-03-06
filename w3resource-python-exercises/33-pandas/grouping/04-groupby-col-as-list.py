import pandas as pd

pd.set_option('display.max_rows', None)

student_data = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("student_data:")
print(student_data)
print()

_result_groupby = student_data.groupby(['school_code'])
print("_result_groupby:")
print(type(_result_groupby))
print(_result_groupby)
print()

_result_list = list(_result_groupby)
print("_result_list:")
print(type(_result_list))
print(_result_list)
print()

for loop_name, loop_data in _result_list:
    print("loop_name=(%s)" % str(loop_name))
    print(loop_data)

