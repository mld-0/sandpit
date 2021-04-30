import numpy as np
import pandas as pd

values = pd.read_excel('employee.xlsx')
print("values:")
print(values)
print()

result = values[(values['hire_date'] >= '2005-01') & (values['hire_date'] <= '2006-12')]
#   or
result = values.query('hire_date >= "2005-01" and hire_date <= "2006-12"')
print("result:")
print(result)

