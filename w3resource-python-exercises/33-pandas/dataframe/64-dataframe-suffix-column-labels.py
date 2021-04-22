import pandas as pd

values = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
print("values:")
print(values)

values = values.add_prefix("A_")
print("Prefix:")
print(values)

values = values.add_suffix("_1")
print("Suffix:")
print(values)

