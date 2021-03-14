import os

path_home = os.path.abspath(os.environ['HOME'])
print(path_home)

#   or

path_home = os.path.expanduser('~')
print(path_home)
