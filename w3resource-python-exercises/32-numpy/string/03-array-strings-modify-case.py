import numpy as np

values = np.array(['python', 'PHP', 'java', 'C++'])
print(values)

capitalized_case = np.char.capitalize(values)
lowered_case = np.char.lower(values)
uppered_case = np.char.upper(values)
swapcased_case = np.char.swapcase(values)
titlecased_case = np.char.title(values)

print("Capitalized: ", capitalized_case)
print("Lowered: ", lowered_case)
print("Uppered: ", uppered_case)
print("Swapcased: ", swapcased_case)
print("Titlecased: ", titlecased_case)

