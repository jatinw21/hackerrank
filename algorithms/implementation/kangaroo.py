#!/usr/bin/env python3

x1, v1, x2, v2 = [int(x) for x in input().split(' ')]


# cases:
# x1 > x2 , v1 > v2 NO
# x1 > x2 , v2 > v1 CAN MEET
# x1 < x2 , v1 > v2 CAN MEET
# x1 < x2 , v2 > v1 NO

flag = 0

if x1 < x2 and v1 > v2:
    while x1 < x2:
         x1 += v1
         x2 += v2
         if x2 == x1:
             flag = 1
             break
elif x1 > x2 and v2 > v1:
    while x2 < x1:
        x1 += v1
        x2 += v2
        if x2 == x1:
            flag = 1
            break

# NOTE: Shorthand conditionals
print("YES") if flag == 1 else print("NO")
