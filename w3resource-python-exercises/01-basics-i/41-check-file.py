import os

def check_file(path_file):
    if os.path.isfile(path_file):
        print(True)
    else:
        print(False)

path_file = "01-twinkle.py"
check_file(path_file)
