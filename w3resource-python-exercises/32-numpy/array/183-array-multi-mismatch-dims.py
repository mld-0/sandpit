import numpy as np

x = 3

a = np.ones((2,2,3))
b = x * np.ones((2,2))

print(a)
print(b)

print(b.shape)
print(b)

#   None or np.newaxis
#   Expands resulting selection by one dimension
print(b[:,:,None].shape)
print(b[:,:,None])

result = a * b[:,:,None]
print(result)
