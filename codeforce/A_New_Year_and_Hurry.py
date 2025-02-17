n, k = map(int, input().split())
count = 0
i = 1
while 240 - k - (i * 5) >= 0 and i <= n:
  k += (i * 5)
  i += 1
  count += 1
print(count)