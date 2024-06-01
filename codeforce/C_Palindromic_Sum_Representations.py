import sys

input = sys.stdin.readline

amount = 5
coins = [i for i in range(1, 4 * (10**4) + 1) if str(i) == str(i)[::-1]]
dp = [0] * (4 * (10 ** 4) + 1)
dp[0] = 1
mod = (10**9 + 7)
def solve(amount):
  mod = (10**9 + 7)

  for coin in coins:
    for i in range(amount - coin + 1):
      dp[coin + i] = (dp[coin + i] + dp[i]) % mod

solve(4 * (10**4))
# print(len(coins))
for _ in range(int(input())):
  print(dp[int(input())]%mod)
# print(dp[-1])
