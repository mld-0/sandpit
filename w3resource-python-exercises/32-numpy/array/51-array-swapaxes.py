import numpy as np

x = np.array([[1,2,3]])
print(x)
y =  np.swapaxes(x,0,1)
print(y)
print()

x = np.arange(3*3).reshape(3,3)
print(x)
y =  np.swapaxes(x,0,1)
print(y)

