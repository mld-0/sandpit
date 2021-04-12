import numpy as np

#   a)  x**2 - 2x + 1
a = [1, -2, 1]
print(a)

#   Old method
result = np.roots(a)
print(result)

#   With polynomial class
p = np.polynomial.Polynomial(a[::-1])  # Note: Polynomial() takes cooefficents in reverse order to np.roots()
result = p.roots()
print(result)
print()

#   b) x**4 - 12x**3 + 10x**2 + 7x - 10
b = [1, -12, 10, 7, -10]
print(b)

#   Old method
result = np.roots(b)
print(sorted(result))  # sort roots, since np.roots() and Polynomial.roots() return results in different order

#   With polynomial class
p = np.polynomial.Polynomial(b[::-1])
result = p.roots()
print(sorted(result))


