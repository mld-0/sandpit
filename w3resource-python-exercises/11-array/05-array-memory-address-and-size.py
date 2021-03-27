from array import array

values = array('i', [2, 3, 5, 7, 11])

print(values)

print("Memory address")
print(values.buffer_info())

print("Buffer size")
values_buffer_size = values.buffer_info()[1] * values.itemsize
print(values_buffer_size)
