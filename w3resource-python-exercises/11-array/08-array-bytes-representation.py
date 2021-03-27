from array import array

values = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
values_bytes = values.tobytes()

print(values)
print(values_bytes)

