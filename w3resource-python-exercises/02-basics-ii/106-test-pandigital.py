
def test_pandigital(value):
    value_digits = set([int(x) for x in str(value)])
    print(len(value_digits) == 10)

test_pandigital(1023456897)
test_pandigital(1023456798)
test_pandigital(1023457689)
test_pandigital(1023456789)
test_pandigital(102345679)

