import numpy as np
import pandas as pd

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

values = pd.DataFrame(exam_data , index=labels)
print("values:")
print(values)

_mapping = {'yes': True, 'no': False}
print("_mapping:")
print(type(_mapping))
print(_mapping)

values['qualify'] = values['qualify'].map(_mapping)
print("Replace yes/no -> True/False")
print(values)
