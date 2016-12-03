#!/usr/bin/env python3

sizeOfMatrix = int(input())

primaryDiagSum = 0
otherDiagSum = 0

for i in range(sizeOfMatrix):
    array = [int(x) for x in input().split(' ')]
    primaryDiagSum += array[i]
    otherDiagSum += array[sizeOfMatrix - (i+1)]

print(abs(primaryDiagSum - otherDiagSum))
