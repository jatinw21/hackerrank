n = int(input())

types = [int(x) for x in input().strip().split(' ')]

typeCounter = [0]*5
for type in types:
    typeCounter[type - 1] +=1

max = typeCounter[0]
maxInd = 0

for i in range(len(typeCounter)):
    if typeCounter[i] > max:
        max = typeCounter[i]
        maxInd = i + 1

print(maxInd)
