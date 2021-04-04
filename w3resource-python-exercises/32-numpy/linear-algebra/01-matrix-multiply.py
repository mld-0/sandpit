import numpy as np

print("2d matricies")
a = np.array([[1, 0], [0, 1]])
b = np.array([[1, 2], [3, 4]])
print(a)
print(b)

#   For 2d arrays, np.dot() and np.matmul() behave the same

#   For n-dimensional, n > 2:
#       For np.matmul(), stacks of matrices are broadcast together as if the matrices were elements.
#       For np.dot(), For N dimensions, is a sum product over the last axis of a and the second-to-last of b

result = np.matmul(a, b)
#   or
result = np.dot(a, b)
#   or
result = a @ b  # '@' invokes matmul()
print(result)
print()

#   LINK: https://stackoverflow.com/questions/34142485/difference-between-numpy-dot-and-python-3-5-matrix-multiplication
#   LINK: https://math.stackexchange.com/questions/63074/is-there-a-3-dimensional-matrix-by-matrix-product
print(">2d matricies")
a = np.random.rand(8,13,13)
b = np.random.rand(8,13,13)
print(a.shape)
print(b.shape)

c = a @ b  # Python 3.5+
d = np.dot(a, b)

print("matmul()")
print(c.shape)
print("dot()")
print(d.shape)
print()

#print(np.allclose(np.einsum('ijk,ijk->ijk', a,b), a*b))        # True 
#print(np.allclose(np.einsum('ijk,ikl->ijl', a,b), a@b))        # True
#print(np.allclose(np.einsum('ijk,lkm->ijlm',a,b), a.dot(b)))   # True
#print()

fourbyfour = np.array([ [1,2,3,4], [3,2,1,4], [5,4,6,7], [11,12,13,14] ])
threebyfourbytwo = np.array([ [[2,3],[11,9],[32,21],[28,17]], [[2,3],[1,9],[3,21],[28,7]], [[2,3],[1,9],[3,21],[28,7]], ])
print(fourbyfour.shape)
print(threebyfourbytwo.shape)

print('4x4*3x4x2 dot:\n {}\n{}\n'.format(np.dot(fourbyfour,threebyfourbytwo).shape, np.dot(fourbyfour,threebyfourbytwo)))
print('4x4*3x4x2 matmul:\n {}\n{}\n'.format(np.matmul(fourbyfour,threebyfourbytwo).shape, np.matmul(fourbyfour,threebyfourbytwo)))

