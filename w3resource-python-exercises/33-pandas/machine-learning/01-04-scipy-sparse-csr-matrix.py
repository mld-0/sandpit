import numpy as np
import pandas as pd
from scipy import sparse

_eye = np.eye(4)
print("_eye:")
print(type(_eye))
print(_eye)
print()

_sparse = sparse.csr_matrix(_eye)
print("_sparse:")
print(type(_sparse))
print(_sparse)
