#!/usr/bin/env python3

num = int(input())

positiveCount, zeroCount, negativeCount = 0, 0, 0

ints = [int(x) for x in input().split(' ')]
for int in ints:
    if int > 0:
        positiveCount += 1
    elif int == 0:
        zeroCount += 1
    else:
        negativeCount += 1

# NOTE: How this print statement works!!
print("%.6f\n%.6f\n%.6f" % (positiveCount/num, zeroCount/num, negativeCount/num))
