import numpy as np
import pandas as pd

values = pd.read_excel('employee.xlsx')
print("values:")
print(values)
print()

result = values.sort_values(by=['first_name', 'last_name'], ascending=[False, True])
print("result:")
print(result)

