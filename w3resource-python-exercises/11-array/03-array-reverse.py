from array import array

values = array('i', [1, 3, 5, 3, 7, 1, 9, 3])

values_reversed = array(values.typecode, values[:])
values_reversed.reverse()

print(values_reversed)

