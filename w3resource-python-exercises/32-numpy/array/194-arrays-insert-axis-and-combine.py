import numpy as np

a = np.random.randint(low=0, high=256, size=(2, 3, 5), dtype=np.uint8)
b = np.random.randint(low=0, high=256, size=(2, 3, 5), dtype=np.uint8)

print(a.shape)
print(a)
print(b.shape)
print(b)

A = a[None, ...]
B = b[None, ...]
#   or
A = np.expand_dims(a, axis=0)
B = np.expand_dims(b, axis=0)

print(A.shape)
print(A)
print(B.shape)
print(B)

result = np.vstack((A, B))
#   or
result = np.append(A, B, axis=0)
print(result.shape)
print(result)


