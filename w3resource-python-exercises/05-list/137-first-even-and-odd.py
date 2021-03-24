
def first_even_and_odd(values):
    _even = None
    _odd = None

    for x in values:
        if x % 2 == 0 and _even is None:
            _even = x
        if x % 2 != 0 and _odd is None:
            _odd = x

    print((_even, _odd))

values = [1, 3, 5, 7, 4, 1, 6, 8]
first_even_and_odd(values)
        
