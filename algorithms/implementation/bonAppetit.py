#!/usr/bin/env python3

n, k = [int(x) for x in input().strip().split(' ')]
prices = [int(x) for x in input().strip().split(' ')]
priceCharged = int(input().strip())

totalPrice = sum(prices)

# print(totalPrice)
totalPrice = totalPrice - prices[k]
# print(totalPrice)
totalPrice = totalPrice/2
# print(totalPrice)
if (totalPrice == priceCharged):
    print("Bon Appetit")
else:
    print(int(priceCharged - totalPrice))
