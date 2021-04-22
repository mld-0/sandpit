import numpy as np
import pandas as pd

df1 = pd.DataFrame({'a':list('aabc'),'b':np.random.randn(4)})
df2 = pd.DataFrame({'a':list('aabc'),'b':np.random.randn(4)})
print("df1:")
print(df1)
print("df2:")
print(df2)
print()

#   validate: Check if merge is specified type
#       1:1     one_to_one      Check keys are unique in both LHS and RHS
#       m:1     many_to_one     Check keys are unique in RHS dataset
#       1:m     one_to_many     Check keys are unique in LHS dataset
#       m:m     many_to_may     Doesn't check keys

#   Fails
#result = pd.merge(df1, df2, on='a', validate='1:1')

#   Valid
#result = pd.merge(df1, df2, on='a', validate='m:m')

result = pd.merge(df1, df2, on='a')
print(result)
