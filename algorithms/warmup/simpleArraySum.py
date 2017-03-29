#!/usr/bin/env python3

n = int(input())
arr = [int(x) for x in input().split(' ')]

sum = 0;
for num in arr:
    sum += num

print(sum)
