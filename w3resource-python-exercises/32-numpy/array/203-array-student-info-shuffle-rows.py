import numpy as np

students = np.array([['stident_id', 'Class', 'Name'], ['01', 'V', 'Debby Pramod'], ['02', 'V', 'Artemiy Ellie'], ['03', 'V', 'Baptist Kamal'], ['04', 'V', 'Lavanya Davide'], ['05', 'V', 'Fulton Antwan'], ['06', 'V', 'Euanthe Sandeep'], ['07', 'V', 'Endzela Sanda'], ['08', 'V', 'Victoire Waman'], ['09', 'V', 'Briar Nur'], ['10', 'V', 'Rose Lykos']]) 
print(students)

#   Using default_rng
students_shuffled = students.copy()
_rng = np.random.default_rng()
_rng.shuffle(students_shuffled[2:8])
print(students_shuffled)

#   Using np.random
students_shuffled = students.copy()
np.random.shuffle(students_shuffled[2:8])
print(students_shuffled)


