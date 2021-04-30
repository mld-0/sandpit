import numpy as np
import pandas as pd

values = pd.read_excel('employee.xlsx')
print("values:")
print(values)
print("values.dtypes:")
print(values.dtypes)
print()

result = values.sort_values('hire_date')
print("result:")
print(result)

