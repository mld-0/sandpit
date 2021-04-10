import numpy as np

values = np.arange(10)
np.random.shuffle(values)
print(values)

n = 3

result = values[np.argsort(values)[-n:]]
print(result)


