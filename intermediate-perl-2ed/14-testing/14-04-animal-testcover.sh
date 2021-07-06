#!/usr/bin/env zsh

cd Animal

perl "Build.pl"
./Build testcover

#	See Animal/cover_dt/coverage.html for results
open "cover_db"

