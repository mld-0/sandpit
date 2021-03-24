
def sort_ints_as_strs(values):
    values_int = [int(x) for x in values]
    values_int_sorted = sorted(values_int)
    print(values_int_sorted)

values = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
sort_ints_as_strs(values)

