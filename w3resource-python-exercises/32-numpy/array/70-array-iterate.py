import numpy as np

x = np.arange(12).reshape(3,4)

for i in np.nditer(x):
    print(i, end=' ')
print()
