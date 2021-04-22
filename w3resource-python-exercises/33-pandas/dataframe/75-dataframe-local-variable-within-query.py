import pandas as pd

values = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print("Original DataFrame")
print(values)

maxx = values["W"].max()
result = values.query("W < @maxx")
print("Values which are less than maximum value of 'W' column")
print(result)

