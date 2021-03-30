import numpy as np
x = np.arange(4)
print(x)

y = np.arange(8).reshape(2,4)
print(y)

for a, b in np.nditer([x,y]):
    print("%d:%d" % (a,b))
