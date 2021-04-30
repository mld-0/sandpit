import numpy as np
import pandas as pd

values = pd.read_excel('coalpublic2013.xlsx', skiprows=3)
print("values:")
print(values)
print()

results = values.query('`Mine Name` == ["Shoal Creek Mine", "Piney Woods Preparation Plant"]')
#   or
results = values[values['Mine Name'].isin(["Shoal Creek Mine", "Piney Woods Preparation Plant"])]
print("results:")
print(results)
