def solve():
  n = int(input())
  nums = [int(i) for i in input().split()]
  s0 = sum(nums)
  if s0 == n:
    print(0)
  elif s0 > n:
    print(s0-n)
  else:
    print(1)
for _ in range(int(input())):
  solve()