import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

values = pd.DataFrame(exam_data , index=labels)
print("Orginal rows:")
print(values)

#   Sort rows by columns
values = values.sort_values(by=['name', 'score'], ascending=[False, True])
#   or
values.sort_values(by=['name', 'score'], ascending=[False, True], inplace=True)
print("Sort by 'name', 'score' (decending, ascending):")
print(values)

values = pd.DataFrame(exam_data , index=labels)

#   Sort columns by rows
values = values.sort_values(by=['a', 'b'], axis=1, ascending=[False, True])
#   or
values.sort_values(by=['a', 'b'], axis=1, ascending=[False, True], inplace=True)
print("Sort by 'a', 'b' (decending, ascending)):")
print(values)

