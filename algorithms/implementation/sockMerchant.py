from collections import defaultdict
import math

n = int(input())
numList = [int(x) for x in input().strip().split(' ')]

numCount = defaultdict(int)

for num in numList:
    numCount[num] += 1

pairs = 0
for key in numCount:
    pairs += math.floor(numCount[key]/2)

print(pairs)
