import numpy as np

values = np.array(['python exercises', 'PHP', 'java', 'C++'])
print(values)

values_encoded = np.char.encode(values)
print(values_encoded)

values_decoded = np.char.decode(values_encoded)
print(values_decoded)


