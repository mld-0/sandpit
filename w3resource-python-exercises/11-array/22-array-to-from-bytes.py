from array import array

array1 = array('i', [7, 8, 9, 10])
array1_bytes = array1.tobytes()

print(array1)
print(array1_bytes)

array2 = array('i', [])
array2.frombytes(array1_bytes)

print(array2)
