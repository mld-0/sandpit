import numpy as np

values = np.array(['2', '11', '234', '1234', '12345'])
print(values)

_n = 5
print(_n)

result = np.char.zfill(values, _n)
print(result)

