import pandas as pd

ds = pd.Series([1,3,5,7,9,11,13,15], index=[0,1,2,3,4,5,7,8])

print("series:")
print(ds)

print("row 2:")
result = ds.iloc[[2]]  # Note: iloc[2] returns an integer, iloc[[2]] returns a series
#   or 
result = ds.take([2], axis=0)
print(type(result))
print(result)

print("row 4:")
result = ds.iloc[[4]]
#   or
result = ds.take([4], axis=0)
print(result)

df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_of_birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32]})

print("dataframe:")
print(df)

print("row 2:")
result = df.iloc[[2]]  # Note: iloc[2] returns a series, iloc[[2]] returns a dataframe
#   or 
result = df.take([2], axis=0)
print(result)
print("row 4:")
result = df.iloc[[4]]
#   or
result = df.take([4], axis=0)
print(result)

