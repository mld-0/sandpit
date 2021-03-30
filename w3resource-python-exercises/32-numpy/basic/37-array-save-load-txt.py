import numpy as np
import os
from tempfile import TemporaryDirectory

a = np.arange(12).reshape(4, 3)

tmpdirname = TemporaryDirectory()
filename_a = os.path.join(tmpdirname.name, 'temp_array.txt')

header = 'col1 col2 col3'
np.savetxt(filename_a, a, fmt='%d', header=header)

b = np.loadtxt(filename_a)

print(a)
print(b)

tmpdirname.cleanup()


