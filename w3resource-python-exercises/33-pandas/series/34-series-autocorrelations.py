import numpy as np
import pandas as pd

_len = 7

values = pd.Series(np.arange(_len) + np.random.normal(1,10,_len))
print("values:")
print(values.to_list())

result = [values.autocorr(i).round(4) for i in range(_len-1)]

print("result:")
print(result)
