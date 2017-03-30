#!/usr/bin/env python3

n, k = [int(x) for x in input().strip().split(' ')]
nums = [int(x) for x in input().strip().split(' ')]

ans = 0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if (nums[i] + nums[j]) % k == 0:
            ans += 1

print(ans)
