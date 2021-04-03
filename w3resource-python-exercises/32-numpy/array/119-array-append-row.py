import numpy as np    

values = np.empty((0,3), int)
print(values)

values = np.append(values, np.array([[10,20,30]]), axis=0)
values = np.append(values, np.array([[40,50,60]]), axis=0)

print(values)
