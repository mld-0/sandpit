setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])

print(setx)
print(sety)
print(setz)

print("If x is subset of y")
print(setx <= sety)
#   or
#print(setx.issubset(sety))

print("If y is subset of x")
print(sety <= setx)
#print(sety.issubset(setx))

print("If y is subset of z")
print(sety <= setz)
#print(sety.issubset(setz))

print("If z is subset of y")
print(setz <= sety)
#print(setz.issubset(sety))

