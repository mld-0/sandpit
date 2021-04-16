import numpy as np

values = np.array([['Python', 'NumPy', 'Exercises'], ['Python', 'Pandas', 'Exercises'], ['Python', 'Machine learning', 'Python']])
print(values)

_word = 'Python'
print(_word)

result_count = np.char.count(values, _word)
print(result_count)

