import numpy as np
import pandas as pd

values = pd.DataFrame({ 'Name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill'], 'Date_Of_Birth ': ['17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'], 'Age': [18.5, 21.2, 22.5, 22, 23] })
print("values:")
print(values)
print()

result_code, result_unique = pd.factorize(values['Name'])
print("result_code:")
print(result_code)
print("result_unique:")
print(result_unique)

