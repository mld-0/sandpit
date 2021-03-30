import numpy as np

p1 = np.array([1,2,3])
p2 = np.array([4,5,6])
print(p1)
print(p2)

d = np.linalg.norm(p2-p1)
print(d)
