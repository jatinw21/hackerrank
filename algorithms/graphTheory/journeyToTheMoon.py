#!/usr/bin/env python3

numAst, numRel = [int(x) for x in input().split(' ')]

countryCounter = 0

countryMembers = []
countryMembers.append({int(x) for x in input().split(' ')})
countryCounter += 1

for i in range(1, numRel):
    currMem1, currMem2 = [int(x) for x in input().split(' ')]

    for j in range(len(countryMembers)):
        # check if currMem1 or currMem2 is in set countryMembers[j]
        if currMem1 in countryMembers[j] or currMem2 in countryMembers[j]:
            countryMembers[j].update([currMem1, currMem2])
            break
    else:
        # loop fell through without finding these in any existing country
        countryMembers.append({currMem1, currMem2})
        countryCounter += 1

print(countryMembers)
listOfNumSame = [len(countryMembers[i]) for i in range(countryCounter)]
print(listOfNumSame)

numAstInSame = 0
for i in listOfNumSame:
    numAstInSame += i

astWithNoSameCountry = numAst - numAstInSame

# these many times append 1 to the list len
for i in range(astWithNoSameCountry):
    listOfNumSame.append(1)

ans = 0
# Do calculation
print("After update.", listOfNumSame)

for i in range(len(listOfNumSame)):
    for j in range(i+1,len(listOfNumSame)):
        ans += listOfNumSame[i]*listOfNumSame[j]

print(ans)
