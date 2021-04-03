import numpy as np

nums = np.array([1,0,2,0,3,0,4,5,6,7,8])

result = list(zip(*np.where(nums == 0)))
print(result)

