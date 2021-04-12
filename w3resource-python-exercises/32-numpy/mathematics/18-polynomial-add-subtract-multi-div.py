import numpy as np

x = (10, 20, 30)
y = (30, 40, 50)
print("x", x)
print("y", y)

p_x = np.polynomial.Polynomial(x)
p_y = np.polynomial.Polynomial(y)

print("add")
p_add = np.polynomial.polynomial.polyadd(x,y)
print(p_add)  # Note: polyadd returns coefficents, whereas p_x + p_y returns a Polynomial instance (hence p.coef in print statement, to make outputs match)
#   or
p_add = p_x + p_y
print(p_add.coef)

print("sub")
p_sub = np.polynomial.polynomial.polysub(x,y)
print(p_sub)  
#   or
p_sub = p_x - p_y
print(p_sub.coef)

print("mul")
p_mul = np.polynomial.polynomial.polymul(x,y)
print(p_mul)
#   or
p_mul = p_x * p_y
print(p_mul.coef)
print()

x = (1, 2, 3, 4)
y = (3, 2, 1)
print("x", x)
print("y", y)
#   Mathematical result is: 4x-5, remainder 16
#   or 4x-5 + 16/(x**2 + 2*x + 3)
print("div")
p_div = np.polynomial.polynomial.polydiv(x,y)  
print(p_div)
#p_div = p_x / p_y  # Invalid
#print(p_div)

