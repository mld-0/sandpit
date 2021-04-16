import numpy as np

values = np.arange(9).reshape((3,3))
print(values)

_weights = [1/4, 2/4, 2/4]
print(_weights)

result = np.average(values, axis=0, weights=_weights)
print(result)

result = np.average(values, axis=1, weights=_weights)
print(result)


