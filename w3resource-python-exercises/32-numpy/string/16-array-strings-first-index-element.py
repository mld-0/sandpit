import numpy as np

values = np.array(['Python', 'PHP', 'JS', 'EXAMPLES', 'HTML'])
print(values)

_c = 'P'
print(_c)

result_index = np.char.find(values, _c)
print(result_index)

