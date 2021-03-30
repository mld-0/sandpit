import numpy as np

x = np.zeros((3,), dtype=('i4,f4,a40'))
print(x)

new_data = [(1, 2., "Albert Einstein"), (2, 2., "Edmond Halley"), (3, 3., "Gertrude B. Elion")]

x[:] = new_data
print(x)
