import numpy as np

def array_contains_row(a, b):
    #   LINK: https://stackoverflow.com/questions/14766194/testing-whether-a-numpy-array-contains-a-given-row
    # Unfortunatly you need to use structured arrays:
    _sorted = np.ascontiguousarray(a).view([('', a.dtype)] * a.shape[-1]).ravel()
    # Actually at this point, you can also use np.in1d, if you already have many b
    # then that is even better.
    _sorted.sort()
    b_comp = np.ascontiguousarray(b).view(_sorted.dtype)
    ind = _sorted.searchsorted(b_comp)
    return _sorted[ind] == b_comp

values = np.arange(20).reshape(4,5)
print(values)

a = [0, 1, 2, 3, 4]
#a = [0, 2, 1, 3, 4]
b = [15, 16, 17, 18, 19]
c = [1, 2, 5, 4, 1]

print(a in values.tolist())
print(b in values.tolist())
print(c in values.tolist())

print(any((values[:] == a).all(1)))
print(any((values[:] == b).all(1)))
print(any((values[:] == c).all(1)))

print(array_contains_row(values, a))
print(array_contains_row(values, b))
print(array_contains_row(values, c))

