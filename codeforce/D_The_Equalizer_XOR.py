import math


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  bits = [0] * 30
  for num in nums:
    i = 0
    while num > 0:
      if num & 1:
        bits[i] += 1
      i += 1
      num >>= 1
  i = 0
  gcd = 0
  while i < 30:
    if bits[i]:
      gcd = bits[i]
      i+= 1
      break
    i += 1
  while i < 30:
    if bits[i]:
      gcd = math.gcd(gcd, bits[i])
    i += 1
  if gcd > 1:
    print("YES")
  else:
    print("NO")