import numpy as np

students =  np.array([['01', 'V', 'Debby Pramod', 30.21], ['02', 'V', 'Artemiy Ellie', 29.32], ['03', 'V', 'Baptist Kamal', 31.00], ['04', 'V', 'Lavanya Davide', 30.22], ['05', 'V', 'Fulton Antwan', 30.21], ['06', 'V', 'Euanthe Sandeep', 31.00], ['07', 'V', 'Endzela Sanda', 32.00], ['08', 'V', 'Victoire Waman', 29.21], ['09', 'V', 'Briar Nur', 30.00], ['10', 'V', 'Rose Lykos', 32.00]])
print(students)

_char_search = 'E'
result_search = students[np.char.startswith(students[:, 2], _char_search)]
result_sum = result_search[:,3].astype(float).sum()
print(_char_search)
print(result_search)
print(result_sum)

_char_search = 'D'
result_search = students[np.char.startswith(students[:, 2], _char_search)]
result_sum = result_search[:,3].astype(float).sum()
print(_char_search)
print(result_search)
print(result_sum)


