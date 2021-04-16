import numpy as np

values = np.array(['python exercises', 'PHP', 'java', 'C++'])
print(values)

result = np.char.join('_', values)
print(result)

