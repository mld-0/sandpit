import numpy as np
import pandas as pd

_data = {'col1':['C1','C1','C2','C2','C2','C3','C2'], 'col2':[1,2,3,3,4,6,5]}
values = pd.DataFrame(_data)
print("values:")
print(values)
print()

result = values.groupby('col1')['col2'].apply(list)
print("groupby('col1')['col2'].apply(list)")
print(type(result))
print(result)
print()

#result = values.groupby('col1').groups
#print("groupby('col1').groups")
#print(type(result))
#print(result)
#print()

#result = values.groupby('col1').indices
#print("groupby('col1').indices")
#print(type(result))
#print(result)

