import numpy as np
from tempfile import TemporaryDirectory
import os

tmpdirname = TemporaryDirectory()
path_save = os.path.join(tmpdirname.name, 'test.csv')
print(path_save)

data = np.asarray([ [10,20,30], [40,50,60], [70,80,90] ])

np.savetxt(path_save, data, fmt='%d', delimiter=',')

values = np.loadtxt(path_save, delimiter=',')
print(values)

tmpdirname.cleanup()

