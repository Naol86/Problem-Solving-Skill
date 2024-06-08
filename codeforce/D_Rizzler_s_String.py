s = input()

ans = 0
pre = 0
cur = 0
for c in s:
  if c == 'a':
    ans += pre + 1
    cur += 1
  elif c == 'b':
    pre += cur
    cur = 0
print(ans % (10 ** 9 + 7))