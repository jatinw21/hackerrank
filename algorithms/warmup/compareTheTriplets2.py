#!/usr/bin/env python3

aMarkList = [int(x) for x in input().strip().split(' ')]
bMarkList = [int(x) for x in input().strip().split(' ')]

# print(aMarkList, bMarkList)
aTotal = 0
bTotal = 0

for i in range(3):
    if aMarkList[i] > bMarkList[i]: #remember to cast to int else soln is wrong
        aTotal += 1
    elif bMarkList[i] > aMarkList[i]:
        bTotal += 1
    else:
        pass

print(aTotal, bTotal)
