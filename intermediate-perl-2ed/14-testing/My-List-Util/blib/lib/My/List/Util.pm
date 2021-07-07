package My::List::Util;

use 5.006;
use strict;
use warnings;

=head1 NAME

My::List::Util - The great new My::List::Util!

=head1 VERSION

Version 0.01

=cut

our $VERSION = '0.01';


=head1 SYNOPSIS

Quick summary of what the module does.

Perhaps a little code snippet.

    use My::List::Util;

    my $foo = My::List::Util->new();
    ...

=head1 EXPORT

A list of functions that can be exported.  You can delete this section
if you don't export anything, such as for a purely object-oriented module.

=head1 SUBROUTINES/METHODS

=head2 sum
	sum() taken from intermediate-perl-2ed answers
=cut

sub sum {
	my $result;
	foreach my $num ( grep { /\A-?\d+\.*\d*\z/ } @_ ) {
		$result += $num;
	}
	return $result;
}

=head2 shuffle
	shuffle() taken from intermediate-perl-2ed answers
=cut

sub shuffle {
	my @deck = @_;
	return unless @deck;

	my $i = scalar(@deck);
	while (--$i) {
		my $j = int(rand($i+1));
		@deck[$i,$j] = @deck[$j,$i];
	}
	return @deck;
}

=head1 AUTHOR

Matthew L Davis, C<< <mld.0 at protonmail.com> >>

=head1 BUGS

Please report any bugs or feature requests to C<bug-my-list-util at rt.cpan.org>, or through
the web interface at L<https://rt.cpan.org/NoAuth/ReportBug.html?Queue=My-List-Util>.  I will be notified, and then you'll
automatically be notified of progress on your bug as I make changes.




=head1 SUPPORT

You can find documentation for this module with the perldoc command.

    perldoc My::List::Util


You can also look for information at:

=over 4

=item * RT: CPAN's request tracker (report bugs here)

L<https://rt.cpan.org/NoAuth/Bugs.html?Dist=My-List-Util>

=item * CPAN Ratings

L<https://cpanratings.perl.org/d/My-List-Util>

=item * Search CPAN

L<https://metacpan.org/release/My-List-Util>

=back


=head1 ACKNOWLEDGEMENTS


=head1 LICENSE AND COPYRIGHT

This software is Copyright (c) 2021 by Matthew L Davis.

This is free software, licensed under:

  The Artistic License 2.0 (GPL Compatible)


=cut

1; # End of My::List::Util
