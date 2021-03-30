import numpy as np
import os
from tempfile import TemporaryDirectory

a = np.arange(20)
b = np.arange(20, 40)

tmpdirname = TemporaryDirectory()
filename_save = os.path.join(tmpdirname.name, 'temp_data.npz')

np.savez(filename_save, a=a, b=b)

with np.load(filename_save) as data:
    print(type(data))
    print(data)
    x = data['a']
    y = data['b']
    print(x)
    print(y)

tmpdirname.cleanup()


