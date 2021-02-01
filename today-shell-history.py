
import subprocess
import pprint
_cmd_history = """
#!/bin/zsh --login
export HISTFILE=~/.zsh_history 
export HISTSIZE=1000
fc -R 
fc -l -t '%FT%H:%M:%S%Z' 0 | cut -c 8- 
"""
_cmd_zsh_history = [ '/bin/zsh', '-c', _cmd_history ]
p = subprocess.Popen(_cmd_zsh_history, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
stdout = str(stdout).strip()
result_history = stdout.split('\\n')
#pprint.pprint(result_history)

