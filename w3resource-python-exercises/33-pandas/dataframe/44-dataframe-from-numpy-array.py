import numpy as np
import pandas as pd

#dtype = [('Column1','int32'), ('Column2','float32'), ('Column3','float32')]
_len = 15
_dtypes = [('Column1', 'int32'), ('Column2', 'float32'), ('Column3', 'float32')]
_index = ['Index'+str(i) for i in range(1, _len+1)]

print("_dtypes:")
print(_dtypes)

_data = np.zeros(_len, dtype=_dtypes)

values = pd.DataFrame(_data, index=_index)
print("values:")
print(values)
print("values.dtypes:")
print(values.dtypes)

#   or

values = pd.DataFrame(np.zeros((_len, 3)), columns=['Column1', 'Column2', 'Column3'])
values = values.astype(dtype={'Column1': 'int32', 'Column2': 'float32', 'Column3': 'float32'})
print("values:")
print(values)
print("values.dtypes:")
print(values.dtypes)

