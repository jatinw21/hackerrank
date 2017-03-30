#!/usr/bin/env python3

# the range of numbers is small, only upto 100, so this can be done
numA, numB = [int(x) for x in input().strip().split(' ')]
A = [int(x) for x in input().strip().split(' ')]
B = [int(x) for x in input().strip().split(' ')]

# get all factors of B[0], these are possible x
# for each element in B, check if all x are factors
#   if yes, pass
#   if no, remove the ones which are not
# After this done for each in B

# for each element in X, check if all elements in A are factors,
#   if yes, good
#   if no, remove that x

# now list is the ans
possibleX = []
k = B[0]

# print(B)
for i in range(1, k + 1): # checking for all elements upto half
    if k % i == 0:
        possibleX.append(i) # these are factors of k
# print("possible x")
# print(possibleX)

removeList = []

for n in B[1:]:
    # print("n: " + str(n))
    removeList = []
    for x in possibleX:
        if n % x != 0:
            removeList.append(x)

    # print(n, removeList,possibleX)
    for r in removeList:
        possibleX.remove(r)

    # print(possibleX)
#
#
# print(possibleX)
# print("=========================")
removeSet = set()
for x in possibleX:
    # print("x: " + str(x))
    for a in A:
        if x % a != 0:
            removeSet.add(x)

for r in removeSet:
    possibleX.remove(r)
#
print(len(possibleX))
