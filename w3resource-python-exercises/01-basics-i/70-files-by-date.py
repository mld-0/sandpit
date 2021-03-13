import glob
import os

#   List of files in directory
files_list = glob.glob("*")
print(files_list)

#   Sorted by mtime
files_list_sorted = sorted(files_list, key=os.path.getmtime)
print(files_list_sorted)
