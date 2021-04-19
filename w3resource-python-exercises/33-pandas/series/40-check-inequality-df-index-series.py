import pandas as pd

df_data = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,75,None,80,86], 'Y':[84,94,89,86,86],'Z':[86,97,96,72,83]});
sr_data = pd.Series([68, 75, 86, 80, None]) 

print("Original DataFrame:")
print(df_data)
print("Original Series:")
print(sr_data)

print("result, compare rows")
result = df_data.ne(sr_data, axis=0)
#   or
result = df_data.ne(sr_data, axis='rows')
print(result)

