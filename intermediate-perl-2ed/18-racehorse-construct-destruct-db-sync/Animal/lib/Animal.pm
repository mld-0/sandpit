package Animal;
use Carp qw(croak);

use 5.032;
use strict;
use warnings;

=head1 NAME

Animal - The great new Animal!

=head1 VERSION

Version 0.01

=cut

our $VERSION = '0.01';


=head1 SYNOPSIS

Quick summary of what the module does.

Perhaps a little code snippet.

    use Animal;

    my $foo = Animal->new();
    ...

=head1 EXPORT

A list of functions that can be exported.  You can delete this section
if you don't export anything, such as for a purely object-oriented module.

=head1 SUBROUTINES/METHODS

=head2 speak
=cut

#	Ongoing: 2021-07-07T16:35:51AEST Use $self->name instead of $self in speak()?
sub speak {
	my $self = shift;
	print "A $self goes ", $self->sound, "!\n";
}

#	Constructor
sub named {
	ref(my $class = shift) and croak "Classname needed"; 
	my $name = shift;
	say "name=($name)";
	my $self = { Name => $name, Color => $class->default_color };
	bless $self, $class;
}

sub default_color { 
	'brown' 
}

sub sound {
	die "Subclass must define sound()";
}

sub color {
	my $either = shift; 
	#if (@_) {
	#	$either->set_name(@_);
	#} else {
		ref $either ? $either->{Color} : $either->default_color; 
	#}
}
sub name {
	my $either = shift; 
	#if (@_) {
	#	$either->set_name(@_);
	#} else {
		ref $either ? $either->{Name} : "an unnamed $either"; 
	#}
}

sub set_name {
	ref(my $self = shift) or croak "Can only set_name on instance variable";
	$self->{Name} = shift;
}

sub set_color {
	ref(my $self = shift) or croak "Can only set_color on instance variable";
	$self->{Color} = shift;
}


=head1 AUTHOR

Matthew L Davis, C<< <mld.0 at protonmail.com> >>

=head1 BUGS

Please report any bugs or feature requests to C<bug-animal at rt.cpan.org>, or through
the web interface at L<https://rt.cpan.org/NoAuth/ReportBug.html?Queue=Animal>.  I will be notified, and then you'll
automatically be notified of progress on your bug as I make changes.




=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc Animal


You can also look for information at:

=over 4

=item * RT: CPAN's request tracker (report bugs here)

L<https://rt.cpan.org/NoAuth/Bugs.html?Dist=Animal>

=item * CPAN Ratings

L<https://cpanratings.perl.org/d/Animal>

=item * Search CPAN

L<https://metacpan.org/release/Animal>

=back


=head1 ACKNOWLEDGEMENTS


=head1 LICENSE AND COPYRIGHT

This software is Copyright (c) 2021 by Matthew L Davis.

This is free software, licensed under:

  The Artistic License 2.0 (GPL Compatible)


=cut

1; # End of Animal
