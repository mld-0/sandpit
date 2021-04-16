import numpy as np

student = """01	V	Debby Pramod
02	V	Artemiy Ellie
03	V	Baptist Kamal
04	V	Lavanya Davide
05	V	Fulton Antwan
06	V	Euanthe Sandeep
07	V	Endzela Sanda
08	V	Victoire Waman
09	V	Briar Nur
10	V	Rose Lykos"""
print(student)

_words_split = '\t'

result_lines = [x.split(_words_split) for x in student.splitlines()]
print(result_lines)


