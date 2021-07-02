#!/usr/bin/env zsh

#	Ongoing: 2021-07-02T18:24:14AEST perl, intermediate-perl-2ed, 13, why <doesn't/can't> test-and-build script install to perl local::lib directory, when same commands run <manually> do achieve that desired result?

#	Doesn't install to ~/perl5 ?
#	(Although same commands do when run one-by-one from shell?)
eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib)"
if [[ ! -d "Animal" ]]; then echo "dir Animal not found" > /dev/stderr; exit; fi
cd "Animal"
perl "Build.PL"
./Build test
./Build disttest
./Build dist
#./Build install

