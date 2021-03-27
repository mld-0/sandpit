from array import array

def array_contains_duplicates(values):
    values_set = set(values)
    print(len(values_set) != len(values))

values = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
array_contains_duplicates(values)

