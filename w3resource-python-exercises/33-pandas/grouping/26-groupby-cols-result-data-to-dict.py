import pprint
import numpy as np
import pandas as pd

values = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("values:")
print(values)
print()

_groupby_labels = ['school_code', 'class']

result = list()

for loop_index, loop_df in values.groupby(_groupby_labels):
    #print(loop_index)
    #print(loop_df)
    #print()
    loop_data_dict = dict(zip(_groupby_labels, loop_index))
    loop_other_cols = list()
    for ll_index, ll_data in loop_df.iterrows():
        #print(ll_index)
        #print(ll_data)
        #print()
        ll_data = ll_data.drop(labels=_groupby_labels)
        loop_other_cols.append(ll_data.to_dict())
    loop_data_dict['other_cols'] = loop_other_cols
    result.append(loop_data_dict)

print("result:")
pprint.pprint(result)



