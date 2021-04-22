import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

values = pd.DataFrame(exam_data)
print("values:")
print(values)
print()

_null_indices = values.isnull()
print("_null_indices:")
print(_null_indices)
print()

_null_per_col = _null_indices.sum()
print("_null_per_col:")
print(_null_per_col)
print()

_null_total = _null_per_col.sum()
print("_null_total:")
print(_null_total)

