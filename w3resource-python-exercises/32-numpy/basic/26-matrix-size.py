import numpy as np

m = np.arange(10,22).reshape((3, 4))

print("Original matrix:")
print(m)

print("Number of rows and columns of the said matrix:")
print(type(m.shape))
print(m.shape)

m_rows = m.shape[0]
m_cols = m.shape[1]

print(m_rows, m_cols)
