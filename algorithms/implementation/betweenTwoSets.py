#!/usr/bin/env python3

numA, numB = [int(x) for x in input().strip().split(' ')]
A = [int(x) for x in input().strip().split(' ')]
B = [int(x) for x in input().strip().split(' ')]

# the range of numbers is small, only upto 100, so this can be done
# get all factors of B[0], these are possible x
# for each element in B, check if all x are factors
#   if yes, pass
#   if no, remove the ones which are not
# After this done for each in B

# for each element in X, check if all elements in A are factors,
#   if yes, good
#   if no, remove that x

possibleX = []
k = B[0]

# factors of first element in B for possible X
for i in range(1, k + 1): # checking for all elements upto half
    if k % i == 0:
        possibleX.append(i) # these are factors of k

# removing factors in not in other elements of B
removeList = []
for n in B[1:]:
    removeList = []
    for x in possibleX:
        if n % x != 0:
            removeList.append(x)

    for r in removeList:
        possibleX.remove(r)

# removing the x which do not have all elements of A as factors
removeSet = set()
for x in possibleX:
    for a in A:
        if x % a != 0:
            removeSet.add(x)

for r in removeSet:
    possibleX.remove(r)

print(len(possibleX))
