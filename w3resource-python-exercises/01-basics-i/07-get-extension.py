import os
input_filename = input("Enter filename:\n")
#   os.path.splitext()
#       returns a tuple that represents root and ext part of the specified path name.
input_extension = os.path.splitext(input_filename)[1]
print(input_extension)
