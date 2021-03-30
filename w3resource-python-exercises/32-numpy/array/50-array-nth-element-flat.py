import numpy as np

x = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
print(x)

e1 = x.flat[3]
print("flat[3] element:")
print(e1)
