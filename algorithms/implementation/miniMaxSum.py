#!/usr/bin/env python3

intList = [int(x) for x in input().split(' ')]

min = intList[0]
max = intList[0]
totSum = 0

for i in intList:
    totSum += i
    if i < min:
        min = i
    if i > max:
        max = i

print(totSum - max, totSum - min)
