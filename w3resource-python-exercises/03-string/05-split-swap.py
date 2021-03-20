
def split_swap(a, b):
    a, b = b[0:2] + a[2:], a[0:2] + b[2:]
    print(a + ' ' + b)

split_swap('abc', 'xyz')
