import numpy as np
import os
from tempfile import TemporaryDirectory

a = np.arange(20)

tmpdirname = TemporaryDirectory()
filename_a = os.path.join(tmpdirname.name, 'temp_array.npy')

np.save(filename_a, a)

b = np.load(filename_a)

print(a)
print(b)

tmpdirname.cleanup()

