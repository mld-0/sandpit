import numpy as np
import sys

nums = np.arange(2000)
print(nums)

np.set_printoptions(threshold=sys.maxsize)
print(nums)
