
def list_tuples_to_list_str(values):
    result = [' '.join([x for x in L]) for L in values]
    print(result)

values = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
list_tuples_to_list_str(values)

values = [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]
list_tuples_to_list_str(values)

