import pandas as pd

values = pd.Series([100, 200, 'python', 300.12, 400])
print("values:")
print(values)

new_data = pd.Series([500, 'php'])
print("new_data:")
print(new_data)

values = values.append(new_data)
print("values, appended new_data:")
print(values)

