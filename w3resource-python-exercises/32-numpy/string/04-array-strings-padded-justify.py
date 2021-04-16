import numpy as np

values = np.array(['python exercise', 'PHP', 'java', 'C++'])
print(values)

centered = np.char.center(values, 15, fillchar='_')
left = np.char.ljust(values, 15, fillchar='_')
right = np.char.rjust(values, 15, fillchar='_')

print("Centered =", centered)
print("Left =", left)
print("Right =", right)

