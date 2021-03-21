
def bytearray_to_hex(_str):
    _str_bytes = bytes(_str)
    result = ''.join(['{:02x}'.format(x) for x in _str_bytes])
    print(result)

list_val = [111, 12, 45, 67, 109] 
bytearray_to_hex(list_val)

