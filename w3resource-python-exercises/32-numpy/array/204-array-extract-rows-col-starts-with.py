import numpy as np

students =  np.array([['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']])
print(students)

_char_search = 'E'
print(_char_search)

#   Get rows where column 2 starts with _char_search
_result_indices = np.char.startswith(students[:, 2], _char_search)
result = students[_result_indices]
print(result)

_char_search = '1'
print(_char_search)

#   Get rows where column 0 starts with _char_search
_result_indices = np.char.startswith(students[:, 0], _char_search)
result = students[_result_indices]
print(result)

