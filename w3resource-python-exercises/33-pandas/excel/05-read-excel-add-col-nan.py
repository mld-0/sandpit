import numpy as np
import pandas as pd

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
values.insert(3, 'column1', np.nan)

print("values:")
print(values)

