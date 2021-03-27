from array import array

values = array('i', [])

values_list = [1, 2, 6, -8]
values.extend(values_list)

print(values)
