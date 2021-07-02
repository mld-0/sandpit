#!/usr/bin/env zsh

#	TODO: 2021-07-02T18:47:03AEST perl, intermediate-perl-2ed, 13-00-create-module-classes.sh, modify files created in package in-place to add the lines as specified in 'Barnyard Summary' (pg 202), and copy barnyard-sounds 

#	Enable local::lib
#eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib)"

module-starter --module=Animal,Animal::Cow,Animal::Mouse,Animal::Sheep,Animal::Horse --minperl=5.032

if [[ ! -d "Animal" ]]; then echo "Animal dir not found" > /dev/stderr; exit; fi
cd "Animal"

if [[ ! -d "script" ]]; then mkdir "script"; fi
cd "script"
#touch "barnyard-sounds.pl"
cp "../../13-02-barnyard-sounds.pl" "barnyard-sounds.pl"

