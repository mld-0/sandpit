import numpy as np

values = np.random.random(15)
print(values)

_index_max = values.argmax()
print(_index_max)

values[_index_max] = -1
print(values)

