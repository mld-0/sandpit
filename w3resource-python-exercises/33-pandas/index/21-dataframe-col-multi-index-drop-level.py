import pandas as pd

cols = pd.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("a", "z")])
values = pd.DataFrame([[1,2,3], [3,4,5], [5,6,7]], columns=cols)
print("values:")
print(values)
print("values.columns:")
print(values.columns)
print()

values.columns = values.columns.droplevel(0)
print("droplevel(0)")
print(values)
print(values.columns)
print()

values = pd.DataFrame([[1,2,3], [3,4,5], [5,6,7]], columns=cols)
print("(reset) values:")
print(values)
print("values.columns:")
print(values.columns)
print()

values.columns = values.columns.droplevel(1)
print("droplevel(1)")
print(values)
print(values.columns)





