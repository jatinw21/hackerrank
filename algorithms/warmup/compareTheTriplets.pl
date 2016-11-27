#!/usr/bin/perl

use warnings;
use strict;

my $aMarkLine = <STDIN>;
my @a = split(' ', $aMarkLine);

my $bMarkLine = <STDIN>;
my @b = split(' ', $bMarkLine);

my $aTotal = 0;
my $bTotal = 0;

for (my $i = 0; $i < 3; $i++) {
    if ($a[$i] > $b[$i]) {
        $aTotal++;
    } elsif ($b[$i] > $a[$i]) {
        $bTotal++;
    }
}

print "$aTotal $bTotal";
