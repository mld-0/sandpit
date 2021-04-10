import numpy as np

complex_num = [1 + 2j, 3 - 1j, 3 - 2j, 4 - 3j, 3 + 5j]
print(complex_num)

complex_num_sorted = np.sort_complex(complex_num)
print(complex_num_sorted)
#print()

#   sort by magnitude of complex numbers
_complex_magnitude = np.absolute(complex_num)
_indices_magnitude_sorted = np.argsort(_complex_magnitude)
#print(_indices_magnitude_sorted)
#print(complex_num)

#   Fails?
#print(complex_num[_indices_magnitude_sorted])
