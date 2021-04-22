import pandas as pd

values = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
print("values:")
print(values)

#   Reverse columns
result_rev_cols = values.iloc[:, ::-1]
print("result_rev_cols:")
print(result_rev_cols)

result_rev_rows = values.iloc[::-1]
print("result_rev_rows:")
print(result_rev_rows)

result_rev_rows_reset_index = values.iloc[::-1].reset_index(drop=True)
print("result_rev_rows_reset_index:")
print(result_rev_rows_reset_index)

