import pandas as pd

values_dict = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
print(type(values_dict))
print(values_dict)

values_df = pd.DataFrame(values_dict)
print("DataFrame")
print(type(values_df))
print(values_df)
print()

result = values_df.iloc[:, 0]
print("Series, cols")
print(type(result))
print(result)
print()

result = values_df.iloc[0, :]
print("Series, row")
print(type(result))
print(result)

