import numpy as np

x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])

print(np.append(x, y, axis=1))
#   or
print(np.hstack((x, y)))

