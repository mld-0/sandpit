import numpy as np

#   a)  x**2 - 2x + 1
a = [1, -2, 1]
x = 2
print(a)
print(x)
#   Old method
result = np.polyval(a, x)
print(result)
#   New method
p = np.polynomial.Polynomial(a[::-1])  # Note: Polynomial() takes cooefficents in reverse order to np.polyval()
result = p(x)
print(result)
print()

#   b) x**4 - 12x**3 + 10x**2 + 7x - 10
b = [1, -12, 10, 7, -10]
x = 3
print(b)
print(x)
#   Old method
result = np.polyval(b, x)
print(result)
#   New method
p = np.polynomial.Polynomial(b[::-1])
result = p(x)
print(result)



