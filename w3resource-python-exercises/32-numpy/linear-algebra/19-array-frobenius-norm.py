import numpy as np

values = np.arange(1,10).reshape(3,3)
print(values)

result_norm = np.linalg.norm(values, 'fro')
result_cond = np.linalg.cond(values, 'fro')
print("Frobenius norm")
print(result_norm)
print("Frobenius conditonal number")
print(result_cond)

