import pandas as pd

print("DataFrame: Contains random values:")
df1 = pd.util.testing.makeDataFrame() # contains random values
print(df1)
print(df1.index.dtype)
print(df1.dtypes)
print()

print("DataFrame: Contains missing values:")
df2 = pd.util.testing.makeMissingDataframe() # contains missing values
print(df2)
print(df2.index.dtype)
print(df2.dtypes)
print()

print("DataFrame: Contains datetime values:")
df3 = pd.util.testing.makeTimeDataFrame() # contains datetime values
print(df3)
print(df3.index.dtype)
print(df3.dtypes)
print()

print("DataFrame: Contains mixed values:")
df4 = pd.util.testing.makeMixedDataFrame() # contains mixed values
print(df4)
print(df4.index.dtype)
print(df4.dtypes)

