
nl=$'\n'; tab=$'\t';

#	zsh site-functions, standard directory for completion scripts
path_sitefunctions="/usr/local/share/zsh/site-functions"

_name_greeter_completefile="_greeter"

echo "Create file$nl$tab$path_sitefunctions/$_name_greeter_completefile" > /dev/stderr
shtab greeter.__main__.parser --shell=zsh > "$path_sitefunctions/$_name_greeter_completefile"

