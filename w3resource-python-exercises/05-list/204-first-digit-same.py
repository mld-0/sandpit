
def first_digit_same(values):
    first_digit = str(values[0])[0]
    result = all([str(x)[0] == first_digit for x in values])
    print(result)

values = [1234, 122, 1984, 19372, 100]
first_digit_same(values)

values = [1234, 922, 1984, 19372, 100]
first_digit_same(values)

values = ['aabc', 'abc', 'ab', 'a']
first_digit_same(values)

values = ['aabc', 'abc', 'ab', 'ha']
first_digit_same(values)

