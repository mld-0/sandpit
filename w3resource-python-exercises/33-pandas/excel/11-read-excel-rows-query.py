import numpy as np
import pandas as pd

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
print("values:")
print(values)
print()

result = values[values['Labor Hours'] > 20000]
#   or
result = values.query('`Labor Hours` > 20000')
print("result:")
print(result)


