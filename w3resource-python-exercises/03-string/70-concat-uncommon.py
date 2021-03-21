
def concat_uncommon(a, b):
    a_not_b = [x for x in a if x not in b]
    b_not_a = [x for x in b if x not in a]
    result = ''.join(a_not_b) + ''.join(b_not_a)
    print(result)

concat_uncommon("abcdpqr", "xyzabcd")
