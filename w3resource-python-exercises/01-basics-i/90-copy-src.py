import os
path_file = os.path.abspath(__file__)
with open(path_file, 'r') as f:
    print(f.read())
