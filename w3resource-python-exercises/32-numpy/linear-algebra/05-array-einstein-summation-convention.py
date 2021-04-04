import numpy as np

#a = np.array([1,2,3])
#b = np.array([0,1,0])
#print("Original 1-d arrays:")
#print(a)
#print(b)
#result =  np.einsum("n,n", a, b)
#print("Einstein’s summation convention of the said arrays:")
#print(result)
#print()
#
#x = np.arange(9).reshape(3, 3)
#y = np.arange(3, 12).reshape(3, 3)
#print("Original Higher dimension:")
#print(x)
#print(y)
#result = np.einsum("mk,kn", x, y)
#print("Einstein’s summation convention of the said arrays:")
#print(result)

#   LINK: https://ajcr.net/Basic-guide-to-einsum/

#   Example: Multiply A and B elementwise (broadcasting A), then sum along axis=1
A = np.array([0, 1, 2])
B = np.array([[ 0,  1,  2,  3], [ 4,  5,  6,  7], [ 8,  9, 10, 11]])
#print(A[:, None])
#print(B)
#print(A[:, None] * B)
#print()
result = (A[:, None] * B).sum(axis=1)
#   or
result = np.einsum('i,ij->i', A, B)
print(result)
print()

#   Example: multiplication of 2d arrays
#>%     np.einsum('ij,jk->ik', A, B)
A = np.array([[1, 1, 1], [2, 2, 2], [5, 5, 5]])
B = np.array([[0, 1, 0], [1, 1, 0], [1, 1, 1]])
result = np.einsum('ij,jk->ik', A, B)
#   or
result = A @ B
print(result)

#   ->  splits equation into LHS/RHS
#   ij and jk label A and B respectively, and ik labels the (single) output array.
#   The expression 'ij,jk->ik' transforms two 2d arrays into a 2d array
#   This requires the axis label by j on A and B to be the same length

#   1)  Repeating letters between input arrays means that values along those axes will be multiplied together. The products make up the values for the output array.
#   2)  Omitting a letter from the output means that values along that axis will be summed.
#   3)  We can return the unsummed axes in any order we like.

#   If we leave out '->' numpy will take the labels that appeared once and arange them in alphabetical order for the RHS
#   That is, 'ij,jk->ik' is equivelent to 'ij,jk'

#   'ij,jk->ki' produces output that is the transpose of 'ij,jk->ik'

#   einsum des not promote datatypes when summing

#   einsum allows '...' to label axes <>

#   Anything that involves combinations of multiplying and summing axes can be written using einsum.

#   Example einsum operations and their equivelents
#   Let A, B be two 1d arrays of compatible shape (either equal lengths, or one of them has length 1)
#       einsum()                Equivelent          Description
#       ('i', A)                A                   Return view of A
#       ('i->', A)              sum(A)              Sum the values of A
#       ('i,i->i', A, B)        A * B               elementwise multiplication of A and B
#       ('i,i', A, B)           inner(A,B)          inner product of A and B
#       ('i,j->ij', A, B)       outer(A, B)         outer product of A and B

#   Let A and B be two 2d arrays with compatible shapes 
#       einsum()                Equivelent                      Description
#       ('ij', A)               A                               View of A
#       ('ji', A)               A.T                             Transpose of A
#       ('ii->i', A)            diag(A)                         Main diagonal of A
#       ('ii', A)               trace(A)                        Sum main diagonal of A
#       ('ij->', A)             sum(A)                          Sum values of A
#       ('ij->j', A)            sum(A, axis=0)                  Sum down columns (across rows) of A
#       ('ij->i', A)            sum(A, axis=1)                  Sum along rows (across columns) of A
#       ('ij,ij->ij', A, B)     A * B                           Elementwise multiplication of A, B
#       ('ij,ji->ij', A, B)     A * B.T                         Elementwise multiplication of A and transpose of B
#       ('ij,kj', A, B)         dot(A, B)                       Matrix multiplication of A, B
#       ('ij,kj->ik', A, B)     inner(A, B)                     Inner product of A, B
#       ('ij,kj->ikj', A, B)    A[:, None] * B                  Each row of A multiplied by B
#       ('ij,kl->ijkl', A, B)   A[:, :, None, None] * B         Each value of A multiplied by B
       


