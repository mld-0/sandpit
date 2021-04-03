import numpy as np

def array_dims_same(a, b):
    if a.shape == b.shape:
        print("Same")
    else:
        print("Different")

a = np.arange(4*5).reshape(4,5)
print(a)

b = np.arange(5*4).reshape(5,4)
print(b)

array_dims_same(a, a)
array_dims_same(a, b)
