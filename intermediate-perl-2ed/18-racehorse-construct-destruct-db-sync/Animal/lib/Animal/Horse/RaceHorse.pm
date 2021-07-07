package Animal::Horse::RaceHorse;
use parent qw(Animal::Horse);

use 5.032;
use strict;
use warnings;

#use Exporter qw(import);

=head1 NAME

Animal::Horse::RaceHorse - The great new Animal::Horse::RaceHorse!

=head1 VERSION

Version 0.01

=cut

our $VERSION = '0.01';


=head1 SYNOPSIS

Quick summary of what the module does.

Perhaps a little code snippet.

    use Animal::Horse::RaceHorse;

    my $foo = Animal::Horse::RaceHorse->new();
    ...

=head1 EXPORT

A list of functions that can be exported.  You can delete this section
if you don't export anything, such as for a purely object-oriented module.

=head1 SUBROUTINES/METHODS

=head2 function1

=cut

sub function1 {
}

=head2 function2

=cut

sub function2 {
}

#	Ongoing: 2021-07-07T17:56:03AEST perl, intermediate-perl-2ed, 18, use of databases, dbmopen, via shared 'our %STANDINGS' variable, better approach to update db whenever values are changed? Simultaneous access to db (presumedly) not an issue unless destructors are being run in parallel -> dbmopen is archaic, and this could be replaced with a 'better' example on how to use databases with perl.

#	Connect %STANDINGS to db 'standings.db'
dbmopen (our %STANDINGS, "standings", 0666) or die "Cannot access standings dbm: $!\n";

#	Constructor: Set values qw(wins places shows losses) to values in db if found at $self->name
sub named {
	my $self = shift;
	$self = $self->SUPER::named(@_);
	my @standings;
	if ($STANDINGS{$self->name}) {
		@standings = split ' ', $STANDINGS{$self->name};
	} else { 
		@standings = split ' ', "0 0 0 0"; 
	}
	@$self{qw(wins places shows losses)} = @standings;
	return $self;
}

#	Destructor: Save qw(wins places shows losses) to db as $self->name
sub DESTROY {
	my $self = shift;
	$STANDINGS{$self->name} = "@$self{qw(wins places shows losses)}";
	$self->SUPER::DESTROY if $self->can( 'SUPER::DESTROY' );
}

sub won { shift->{wins}++; }
sub placed { shift->{places}++; }
sub showed { shift->{shows}++; }
sub lost { shift->{losses}++; }

sub standings {
	my $self = shift;
	join ", ", map "$self->{$_} $_", qw(wins places shows losses);
}

=head1 AUTHOR

Matthew L Davis, C<< <mld.0 at protonmail.com> >>

=head1 BUGS

Please report any bugs or feature requests to C<bug-animal at rt.cpan.org>, or through
the web interface at L<https://rt.cpan.org/NoAuth/ReportBug.html?Queue=Animal>.  I will be notified, and then you'll
automatically be notified of progress on your bug as I make changes.




=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc Animal::Horse::RaceHorse


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

1; # End of Animal::Horse::RaceHorse
