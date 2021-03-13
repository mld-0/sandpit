import os
import time
import platform

filename = '01-twinkle.py'

mtime = time.ctime(os.path.getmtime(filename))
ctime = time.ctime(os.path.getctime(filename))

#   Can't get creation time on MacOS?

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

print(mtime)
print(ctime)

ctime = time.ctime(creation_date(filename))
print(ctime)


