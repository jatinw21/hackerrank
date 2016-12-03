#!/usr/bin/perl

my $numItems = <STDIN>;
my $intLine =<STDIN>;

my @ints = split(/ /, $intLine);

my $sum = 0;
for my $int (@ints) {
    $sum += $int;
}

print($sum);
