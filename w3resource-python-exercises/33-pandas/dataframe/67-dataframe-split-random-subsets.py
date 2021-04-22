import pandas as pd
df = pd.DataFrame({ 'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton'], 'date_of_birth': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'], 'age': ['18', '21', '22', '22', '23'] })

df_1 = df.sample(frac = 0.6)
df_2 = df.drop(df_1.index)

print("Original Dataframe and shape:")
print(df)
print(df.shape)

print("Subset-1 and shape:")
print(df_1)
print(df_1.shape)

print("Subset-2 and shape:")
print(df_2)
print(df_2.shape)

