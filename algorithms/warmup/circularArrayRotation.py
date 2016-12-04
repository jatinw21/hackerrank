#!/usr/bin/env python3

numInts, numRotations, numQueries = [int(x) for x in input().split(' ')]
# DEBUG:
# print(numInts, numRotations, numQueries)

intList = [int(x) for x in input().split(' ')]
for j in range(numQueries):
    query = int(input())
    # http://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
    # NOTE: for copying such that changing copy doesn't affect original, slicing is fastes
    # NOTE: But if original list contains list, dictionaries or class instances, changing them would change in original,
    # NOTE: so for that we need copy.deepcopy(old_list)
    listCopy = intList[:]
    for i in range(numRotations):
        removed = listCopy.pop()
        listCopy.insert(0, removed)
    print(listCopy[query])
