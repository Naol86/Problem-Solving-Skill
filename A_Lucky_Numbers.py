n, k = map(int, input().split())

nums = [i for i in input().split()]
ans = 0
for x in nums:
  count = 0
  for s in x:
    if s in {'4', '7'}:
      count += 1
    if count > k:
      break
  else:
    ans += 1
print(ans)