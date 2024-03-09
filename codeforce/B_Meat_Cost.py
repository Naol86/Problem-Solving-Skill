import sys
input = sys.stdin.readline

min_cost = float('inf')
money = 0
for _ in range(int(input())):
    amount, cost = [int(i) for i in input().split()]
    min_cost = min(min_cost, cost)
    money += amount * min_cost
print(money)