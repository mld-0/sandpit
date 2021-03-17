import subprocess
cmd = ['ls', '-1']
subprocess.run(cmd)  # run waits for command to finish, equivelent to combined Popen and communicate calls
