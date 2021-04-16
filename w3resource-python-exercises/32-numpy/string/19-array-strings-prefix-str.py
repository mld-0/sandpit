import numpy as np

values = np.array(['1.12', '2.23', '3.71', '4.23', '5.11'])
print(values)

_str_prefix = '00'
print(_str_prefix)

result = np.char.add(_str_prefix, values)
print(result)

