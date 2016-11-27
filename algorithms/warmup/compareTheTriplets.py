#!/usr/bin/env python3

aMarkList = input().strip().split(' ')
bMarkList = input().strip().split(' ')

# print(aMarkList, bMarkList)
aTotal = 0
bTotal = 0

for i in range(3):
    if int(aMarkList[i]) > int(bMarkList[i]):
        aTotal += 1
    elif int(bMarkList[i]) > int(aMarkList[i]):
        bTotal += 1
    else:
        pass

print(aTotal, bTotal)
