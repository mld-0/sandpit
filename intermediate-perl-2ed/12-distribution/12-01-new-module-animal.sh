#!/usr/bin/env zsh

#	Commands as taken from Ch12 Answers, not-yet-run -> what files/directories need to be created/supplied?
module-starter --module=Animal --author=Gilligan --email="Gilligan@example.net"
cd Animal
perl Build.PL
./Build test
./Build disttest
./Build dist

