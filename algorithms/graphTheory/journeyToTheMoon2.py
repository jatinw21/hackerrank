#!/usr/bin/env python3

numAst, numRel = [int(x) for x in input().split(' ')]
countryCounter = 0

astronaut = [None]*numAst



for i in range(numRel):
    currMem1, currMem2 = [int(x) for x in input().split(' ')]
    astronaut[currMem1] = countryCounter
    astronaut[currMem2] = countryCounter
    countryCounter += 1

print(astronaut)
