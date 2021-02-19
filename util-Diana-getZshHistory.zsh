#!/bin/zsh

hostname="Diana"
ssh $hostname 'cat ~/.zsh_history' > /tmp/zsh_history.$hostname

export HISTSIZE=99999
fc -R /tmp/zsh_history.$hostname
fc -t '%FT%H:%M:%S%Z' -l -20


