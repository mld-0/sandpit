
#   symmetric difference, or disjunctive union
#   elements which are in either of the sets and not in their intersection
#   the symmetric difference of the sets {1,2,3} and {3,4} is {1,2,4}.

setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
#Symmetric difference
setc = setx ^ sety
print(setc)
