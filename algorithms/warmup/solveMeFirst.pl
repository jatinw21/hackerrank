#!/usr/bin/perl

sub Add {
    my ($x,$y) = @_;
    return($x+$y);
}

my $num1 = <STDIN>;
my $num2 = <STDIN>;
my $answer = Add($num1, $num2);
print "$answer";
