use 5.006;
use strict;
use warnings;
use Module::Build;
Module::Build->VERSION('0.4004');

my $builder = Module::Build->new(
    module_name         => 'My::List::Util',
    license             => 'artistic_2',
    dist_author         => q{Matthew L Davis <mld.0@protonmail.com>},
    dist_version_from   => 'lib/My/List/Util.pm',
    release_status      => 'stable',
    configure_requires => {
        'Module::Build' => '0.4004',
    },
    test_requires => {
        'Test::More' => '0',
    },
    requires => {
        #'ABC'              => '1.6',
        #'Foo::Bar::Module' => '5.0401',
    },
    add_to_cleanup     => [ 'My-List-Util-*' ],
);

$builder->create_build_script();
