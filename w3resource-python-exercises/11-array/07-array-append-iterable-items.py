from array import array

values = array('i', [1, 3, 5, 7, 9])
additional_values = [3, 5, 7, 9]

values.extend(additional_values)

print(values)

