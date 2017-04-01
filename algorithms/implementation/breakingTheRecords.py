n = int(input())

scores = [int(x) for x in input().strip().split(' ')]

max = scores[0]
min = scores[0]

maxNum = 0
minNum = 0

for score in scores:
    if score > max:
         max = score
         maxNum += 1

    elif score < min:
         min = score
         minNum += 1

print(maxNum, minNum)
