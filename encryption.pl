#!/usr/bin/perl

use warnings;
use Math::Complex;
use POSIX;

my $line = <>;
$line =~ s/ //g;
# print "$line\n";
chomp $line;
my $l = length "$line";
my ($rows,$cols);
my $lowest  = floor(sqrt($l));
my $highest = ceil(sqrt($l));

# print "$l $lowest $highest\n";
my $min = 9999999999;
my $finalRow;
my $finalCol;
for ($rows = $lowest; $rows <= $highest; $rows++) {
    for ($cols = $rows; $cols <= $highest; $cols++) {
        if ($rows*$cols < $min && $rows*$cols >= $l) {
            $min = $rows*$cols;
            # save final row and column
            $finalRow = $rows;
            $finalCol = $cols;
        }
    }
}
# printf("finalCol: %d\nfinalRow: %d\n", $finalCol, $finalRow);


my @characs = split("", $line);
my $j;
for (my $k = 0; $k < $finalCol; $k++) {# col = 8, row = 7
    $j = $k;
    for (my $i = 0; $i < $finalCol; $i++) {
        if (defined $characs[$j]) {
            print "$characs[$j]";
        }

        $j += $finalCol;
    }
    print " ";
}
