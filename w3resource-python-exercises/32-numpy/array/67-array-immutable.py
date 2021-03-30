import numpy as np
x = np.zeros(10)
x.flags.writeable = False

try:
    x[0] = 1
except ValueError as e:
    print("%s: Can't write to x" % e)

