
bin_cpan=cpan

$bin_cpan Business:ISBN
$bin_cpan JSON
$bin_cpan Regexp::Common
$bin_cpan Regexp::Assemble
$bin_cpan Module::Starter
$bin_cpan Class::MethodMaker
$bin_cpan File::Size
$bin_cpan Crypt::Digest::SHA256
$bin_cpan Module::Install # module-starter<?>
$bin_cpan Module::Starter::AddModule

$bin_cpan local::lib
perl -MCPAN -Mlocal::lib -e 'CPAN::install(LWP)'

$bin_cpan Devel::Cover
$bin_cpan File::Slurp
$bin_cpan lib::relative
$bin_cpan DateTime;
