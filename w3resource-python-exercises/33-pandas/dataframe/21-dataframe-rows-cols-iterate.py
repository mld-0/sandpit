import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

values = pd.DataFrame(exam_data , index=labels)
print("values:")
print(values)

#   Iterate over rows
for loop_index, loop_row_series in values.iterrows():
    print(loop_index)
    print(loop_row_series)
print()
#   or
for loop_row_tuple in values.itertuples():
    print(loop_row_tuple)
print()

#   Iterate over columns
for loop_col_label, loop_col_series in values.iteritems():
    print(loop_col_label)
    print(loop_col_series)
print()
#   or
for loop_col_label, loop_col_series in values.items():
    print(loop_col_label)
    print(loop_col_series)
print()

