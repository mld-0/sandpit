import os
import time

path_script = os.path.abspath('01-twinkle.py')


print('File         :', path_script)
print('Access time  :', time.ctime(os.path.getatime(path_script)))
print('Modified time:', time.ctime(os.path.getmtime(path_script)))
print('Change time  :', time.ctime(os.path.getctime(path_script)))
print('Size         :', os.path.getsize(path_script))

#   or

st = os.stat(path_script)
print(st)
