import numpy as np

values = np.array(['Python\nExercises, Practice, Solution'])
print(values)

result = np.char.splitlines(values)
print(result)

