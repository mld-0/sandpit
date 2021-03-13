import os
import platform

os_name = os.name
os_platform = platform.system()
os_release = platform.release()

print("%s, %s, %s" % (os_name, os_platform, os_release))
