for _ in range(int(input())):
  n, k = map(int, input().split())
  s = input()
  if k == 0:
    print("YES")
    continue
  if n < k * 2 + 1:
    print("NO")
    continue
  left = 0
  right = n - 1
  while left < right:
    if s[left] != s[right]:
      print("NO")
      break
    left += 1
    right -= 1
  else:
    print("YES")