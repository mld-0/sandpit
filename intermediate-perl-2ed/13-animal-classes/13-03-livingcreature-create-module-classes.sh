#!/usr/bin/env zsh

module-starter --distro=LivingCreature --module=LivingCreature,LivingCreature::Animal,LivingCreature::Person

if [[ ! -d "LivingCreature" ]]; then echo "Error, dir not found"; die; fi
cd "LivingCreature";

if [[ ! -d "scripts" ]]; then
	mkdir "scripts";
fi
if [[ ! -e "scripts/person.pl" ]]; then 
	touch "scripts/person.pl";
fi

