import numpy as np

values = np.arange(0,10)
print(values)

result = values.copy()
np.random.shuffle(result)
print(result)
#   or
result = values.copy()
_rng = np.random.default_rng()
_rng.shuffle(result)
print(result)
#   or
result = _rng.permutation(10)
print(result)


