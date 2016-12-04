#!/usr/bin/env python3

# NOTE: BETTER APPROACH WOULD BE TO FIRST SORT THE ORIGINAL LIST COZ THEN
# CLOSEST CAN BE ONLY THE ONES RIGHT NEXT
# Other more time consuming is down below

numInts = int(input())

intLists = [int(x) for x in input().split(' ')]
intLists.sort()

minDiff = abs(intLists[0] - intLists[1])
listAnswer = []
for i in range(numInts-1):
    if abs(intLists[i] - intLists[i+1]) < minDiff:
        minDiff = abs(intLists[i] - intLists[i+1])
        listAnswer = []
        listAnswer.append(intLists[i])
        listAnswer.append(intLists[i+1])
    elif abs(intLists[i] - intLists[i+1]) == minDiff:
        listAnswer.append(intLists[i])
        listAnswer.append(intLists[i+1])

listAnswer.sort()
for int in listAnswer:
    print(int, end=" ")



# REVIEW: NOT SO GOOD METHOD. TIME CONSUMING
# numInts = int(input())
#
# intLists = [int(x) for x in input().split(' ')]
# listAnswer = []
#
# minDiff = abs(intLists[0] - intLists[1])
# for i in range(numInts):
#     for j in range(i+1, numInts):
#         if abs(intLists[i] - intLists[j]) < minDiff:
#             minDiff = abs(intLists[i] - intLists[j])
#             listAnswer = []
#             listAnswer.append(intLists[i])
#             listAnswer.append(intLists[j])
#         elif abs(intLists[i] - intLists[j]) == minDiff:
#             listAnswer.append(intLists[i])
#             listAnswer.append(intLists[j])
# # NOTE: for sorting a list of ints in ascending order
# listAnswer.sort()
#
# for int in listAnswer:
#     print(int, end=" ")
