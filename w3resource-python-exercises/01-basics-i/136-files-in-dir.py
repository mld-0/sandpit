import os
import glob

path_dir = os.path.dirname(os.path.abspath('01-twinkle.py'))
print(path_dir)

files_list = [x for x in glob.glob("*") if os.path.isfile(x)]
#   or
files_list = [x for x in os.listdir(path_dir) if os.path.isfile(x)]
print(files_list)
