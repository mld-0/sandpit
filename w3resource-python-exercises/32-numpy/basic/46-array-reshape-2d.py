import numpy as np   

print(np.arange(1, 151).reshape(15, 10)) 

#   If a single value in reshape is -1, it is infered from the size of the array and the remaining dimensions
print(np.arange(1, 151).reshape(-1, 10)) 

print(np.arange(1, 151).reshape(15, -1))
