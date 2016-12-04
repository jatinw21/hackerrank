#!/usr/bin/env python3

#      'm' apples                   'n' oranges
#       a..........s........t........b
#       <----- d ---->

s, t = [int(x) for x in input().split(' ')]
a, b = [int(x) for x in input().split(' ')]
m, n = [int(x) for x in input().split(' ')]

appleDistances = [int(x) for x in input().split(' ')]
orangeDistances = [int(x) for x in input().split(' ')]

appleCount, orangeCount = 0, 0

for i in range(m):
    # NOTE: also take care that it doesnt overshoot from the other side
    # hence the second condition
    if a + appleDistances[i] >= s and a + appleDistances[i] <= t:
        appleCount += 1
for j in range(n):
    if b + orangeDistances[j] <= t and b + orangeDistances[j] >= s:
        orangeCount += 1

print(appleCount, orangeCount, sep="\n")
