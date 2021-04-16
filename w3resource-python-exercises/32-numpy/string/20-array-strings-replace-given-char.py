import numpy as np

values = np.array([['Python-NumPy-Exercises'], ['-Python-']])
print(values)

_c_find = '-'
_c_replace = '=='

result = np.char.replace(values, _c_find, _c_replace)
print(result)

