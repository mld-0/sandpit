import ctypes
check_result = ctypes.sizeof(ctypes.c_voidp) * 8
#   or
import struct
check_result = struct.calcsize("P") * 8

print("%s bit" % check_result)
