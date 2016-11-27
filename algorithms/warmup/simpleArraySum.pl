#!/usr/bin/perl
use warnings;
use strict;

my @numArray;
my $sum;
my $sizeOfArray = <STDIN>;
# stdin takes a line at a time
my $numArrayLine = <STDIN>;
@numArray = split(/ /,$numArrayLine);

# this even accounts if more numbers are given than specified
for (my $i = 0; $i < $sizeOfArray; $i++) {
    $sum += $numArray[$i];
}
print "$sum";
