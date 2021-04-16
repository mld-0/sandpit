import numpy as np

x = np.array([' python exercises ', ' PHP  ', ' java  ', '  C++'])
print(x)

rstripped_char = np.char.rstrip(x)
print("Remove the trailing whitespaces : ", rstripped_char)

