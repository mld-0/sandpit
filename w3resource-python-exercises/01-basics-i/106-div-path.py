import os

path_script = os.path.abspath('01-twinkle.py')
print(path_script)

extension = os.path.splitext(path_script)[1]
print(extension)
