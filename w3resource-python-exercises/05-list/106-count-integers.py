
def count_integers(values):
    result = len([x for x in values if isinstance(x, int)])
    print(result)

values = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
count_integers(values)
