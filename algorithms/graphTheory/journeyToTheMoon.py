#!/usr/bin/env python3

numAst, numRel = [int(x) for x in input().split(' ')]

countryCounter = 0

countryMembers = []
countryMembers.append({int(x) for x in input().split(' ')})
countryCounter += 1


for i in range(1, numRel):
    matchFound = 0
    currMem1, currMem2 = [int(x) for x in input().split(' ')]
    stage = 0
    for j in range(len(countryMembers)):

            # check if currMem1 or currMem2 is in set countryMembers[j]
        if currMem1 in countryMembers[j] or currMem2 in countryMembers[j]:
            matchFound = 1
            if stage == 0:
                countryMembers[j].update([currMem1, currMem2])
                matchFoundCounter = j
                stage = 1
            else: # already found match, added this to that set, now wherever match is found
            # add that set to the noted set
                countryMembers[matchFoundCounter] = countryMembers[matchFoundCounter].union(countryMembers[j])
                del countryMembers[j]
                countryCounter -= 1
        if matchFound == 0:
            # loop fell through without finding these in any existing country
            countryMembers.append({currMem1, currMem2})
            countryCounter += 1
    # print(countryMembers)

# print(countryMembers)
listOfNumSame = [len(countryMembers[i]) for i in range(countryCounter)]
# print(listOfNumSame)

numAstInSame = 0
for i in listOfNumSame:
    numAstInSame += i

astWithNoSameCountry = numAst - numAstInSame

# 10 5 3 1 1 1 1
# 10*5 + 10*3 + 10*(astWithNoSameCountry) + 5*3 + 5*(astWithNoSameCountry) + 3*(astWithNoSameCountry) + (astWithNoSameCountry)*(astWithNoSameCountry - 1)/2
#





################################################################
# these many times append 1 to the list len
for i in range(astWithNoSameCountry):
    listOfNumSame.append(1)

ans = 0
# Do calculation
# print("After update.", listOfNumSame)

for i in range(len(listOfNumSame)):
    for j in range(i+1,len(listOfNumSame)):
        ans += listOfNumSame[i]*listOfNumSame[j]

print(ans)
