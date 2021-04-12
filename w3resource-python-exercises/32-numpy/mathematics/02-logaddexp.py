import numpy as np

a = np.array([[1, 2], [2, 1]])
b = np.array([[2, 4], [1, 2]])
print("a")
print(a)
print("b")
print(b)

result_e = np.logaddexp(a, b)
print("result_e")
print(result_e)

result_2 = np.logaddexp2(a, b)
print("result_2")
print(result_2)

