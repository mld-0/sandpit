import numpy as np

x = np.array([[20,20,20],[30,30,30],[40,40,40]])
v = np.array([20,30,40])
print(x)
print(v)


#   Require v to be a column vector
z = x / v[:, None]
#   or
z = x / v[..., None]
#   or
z = x / v.reshape(3,1)
#   or
z = x / np.atleast_2d(v).T

print(z)
