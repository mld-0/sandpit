import numpy as np

values = np.array(['Python', 'PHP', 'JS', 'examples', 'html'])
print(values)

_c = 'P'
print(_c)

result_count = np.char.count(values, _c)
print(result_count)

