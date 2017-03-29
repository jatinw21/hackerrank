#!/bin/python

import sys

numArr = [int(x) for x in input().strip().split(' ')]

min = numArr[0]
max = numArr[1]
sum = 0

for num in numArr:
    if num < min:
        min = num

    if num > max:
        max = num

    sum += num

minSum = sum - max
maxSum = sum - min

print(minSum, maxSum)
