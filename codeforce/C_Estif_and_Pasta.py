import math
def pow_me(a, b):
  MOD = 10 ** 9 + 7
  if b == 1:
    return a
  if b % 2:
    return (pow_me(a, b - 1) * a) % MOD
  x = int(pow_me(a, b//2)) % MOD
  return (x * x) % MOD
  # return 1

x = int(input())
if x == 1:
  print(6)
else:
  MOD = 10 ** 9 + 7
  level = int(math.pow(2, x)) - 2
  # print(level)
  ans = pow_me(4, level)
  print((ans * 6) % MOD )