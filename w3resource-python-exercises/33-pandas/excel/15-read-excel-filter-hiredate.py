import numpy as np
import pandas as pd

values = pd.read_excel('employee.xlsx')
print("values:")
print(values)
print("values.dtypes:")
print(values.dtypes)
print()

result = values[values['hire_date'] >='2007-01-01']
print("result:")
print(result)
