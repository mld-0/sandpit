import numpy as np
import pandas as pd

values = pd.read_excel('employee.xlsx')
values = values.set_index(['hire_date'])
print("values:")
print(values)
print()

result = values.loc['2005']
#   or
result = values[values.index.year == 2005]
#   or
result = values.query('index >= "2005" and index < "2006"')
print("result:")
print(result)
