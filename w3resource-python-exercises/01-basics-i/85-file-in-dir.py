import os

path_script = os.path.realpath(__file__)
dir_script = os.path.dirname(path_script)

filename = '01-twinkle.py'

if os.path.isdir(filename):
    print("Dir")
elif os.path.isfile(filename):
    print("File")
