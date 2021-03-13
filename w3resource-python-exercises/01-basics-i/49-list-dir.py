import os

path_dir = "/tmp"

files_list = [x for x in os.listdir(path_dir) if os.path.isfile(os.path.join(path_dir, x))]
print(files_list)

#   or

_, _, files_list = next(os.walk(path_dir))  # detects file-like objects as well as files
print(files_list)
