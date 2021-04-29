import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

values = pd.DataFrame({
    'student_id': ['S001','S001','S002','S002','S003','S003'],
    'marks': [[88,89,90],[78,81,60],[84,83,91],[84,88,91],[90,89,92],[88,59,90]]})

print("values:")
print(values)
print()

result = values.groupby('student_id')['marks'].apply(list)
#   or
result = values.set_index('student_id')['marks'].groupby('student_id').apply(list)
print("result:")
print(result)
print()

result_mean = result.apply(lambda x: np.mean(x,0))
print("result_mean:")
print(result_mean)

