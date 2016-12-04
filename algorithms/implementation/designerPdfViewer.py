#!/usr/bin/env python3

heightList = [int(x) for x in input().split(' ')]

characs = input()

# NOTE: Use this method to split on every n characs. Replace 1 by 'n'
# When we have to break a string characs into a list of its characs
[characs[i:i+1] for i in range(0, len(characs), 1)]

# NOTE: num of elements in a list
length = len(characs)

maxHeight = 0

for i in characs:
    # DEBUG:
    # print(ord(i)-ord('a'))

    # NOTE: use ord() for ASCII value
    if heightList[ord(i)-ord('a')] > maxHeight:
        maxHeight = heightList[ord(i)-ord('a')]

print(length*maxHeight)
