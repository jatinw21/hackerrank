#!/usr/bin/env python3

size = int(input())

# NOTE: python3's print() adds a new line by default
# to not add new line, do print("", end="")
for i in range(size):
    for j in range(size - (i+1)):
        print(" ", end="")
    for k in range(i+1):
        print("#", end="")
    if i == (size - 1):
        break
    print()
