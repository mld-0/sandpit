import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

values = pd.DataFrame(exam_data , index=labels)

#   Number of rows
values_rows = len(values.values)
#   or
values_rows = len(values.index)
#   or
values_rows = len(values.axes[0])
#   or
values_rows = values.shape[0]

#   Number of columns
values_cols = len(values.values[0])
#   or
values_cols = len(values.columns)
#   or
values_cols = len(values.axes[1])
#   or
values_cols = values.shape[1]

print("values_rows:")
print(values_rows)
print("values_cols:")
print(values_cols)
