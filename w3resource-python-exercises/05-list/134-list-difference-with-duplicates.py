from collections import Counter

def list_difference_with_duplicates(a, b):
    _a = a[:]
    _b = b[:]

    i = 0
    while i < len(a) and len(b) > 0:
        aa = a[i]
        if aa in _b:
            _b.remove(aa)
        i += 1
    b_not_a = _b[:]

    i = 0
    while i < len(b) and len(a) > 0:
        bb = b[i]
        if bb in _a:
            _a.remove(bb)
        i += 1
    a_not_b  = _a[:]

    ab_difference = a_not_b + b_not_a
    print(ab_difference)

a = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
b = [1, 1, 2, 4, 5, 6]
list_difference_with_duplicates(a, b)

