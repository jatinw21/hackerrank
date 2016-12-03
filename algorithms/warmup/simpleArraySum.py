#!/usr/bin/env python3

# taking input
sizeOfArray = int(input())
numArrayLine = input()

# DEBUG INFO
# print(numArrayLine, sizeOfArray)

# splitting and putting into list
splitLineList = numArrayLine.split(' ')

# DEBUG INFO
# print(splitLineList)

# going through list and calculating sum

# NOTE: need to first declare sum = 0 before starting adding
sum = 0
for num in splitLineList:
    sum += int(num)
print(sum)
