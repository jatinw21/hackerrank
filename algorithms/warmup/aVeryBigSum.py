#!/usr/bin/env python3

numItems = int(input())
ints = [int(x) for x in input().split(' ')]

sum = 0
for x in ints:
    sum += x
print(sum)
