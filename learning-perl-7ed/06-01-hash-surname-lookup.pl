#!/usr/bin/env perl
use strict;
use warnings;
use v5.032;

my %name_to_surname = ( fred => 'flinstone', barney => 'rubble', wilma => 'flinstone' );

my $input_name = 'barney';
say "input_name=($input_name)";

my $result_surname = $name_to_surname{$input_name};
say "result_surname=($result_surname)";


