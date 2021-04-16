import numpy as np

x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'])
print(x)

lstripped_char = np.char.lstrip(x)
print("Remove the leading whitespaces : ", lstripped_char)

