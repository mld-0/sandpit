import os

path_script = os.path.abspath('01-twinkle.py')
print(path_script)

if os.path.isfile(path_script):
    print("file")    
if os.path.isdir(path_script):
    print("dir")
if os.path.isabs(path_script):
    print("abs path")
if os.path.islink(path_script):
    print("link")
if os.path.exists(path_script):
    print("exists")
if os.path.lexists(path_script):
    print("link exists")

