import numpy as np 

values = np.array(['Python', 'PHP', 'JS', 'Examples', 'html5', '5'])
print(values)

r1 = np.char.isdigit(values)
r2 = np.char.islower(values)
r3 = np.char.isupper(values)

print("Digits only =", r1)
print("Lower cases only =", r2)
print("Upper cases only =", r3)

