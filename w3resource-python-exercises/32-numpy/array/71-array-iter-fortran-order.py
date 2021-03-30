import numpy as np

x = np.arange(12).reshape(3, 4)

#   In Fortran the first index is the most rapidly varying index when moving through the elements of a two dimensional array as it is stored in memory.

for x in np.nditer(x, order="F"):
    print(x,end=' ')
print()
