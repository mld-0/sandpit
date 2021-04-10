import numpy as np

m = np.array([[3,2],[1,0]])
print(m)

w, v = np.linalg.eig(m) 
print("Eigenvalues")
print(w)
print("Eigenvectors")
print(v)
