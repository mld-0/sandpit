import os
filename = '01-twinkle.py'

filesize = os.stat(filename).st_size
#   or
filesize = os.path.getsize(filename)

print(filesize)  # bytes
