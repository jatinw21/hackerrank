#!/usr/bin/env python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]


max = height[0]
maxCounter = 1

for n in height[1:]:
    if n > max:
        max = n
        maxCounter = 1

    elif n == max:
        maxCounter += 1

print(maxCounter)
