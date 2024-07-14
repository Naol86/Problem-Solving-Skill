for _ in range(int(input())):
  x = int(input())
  s = input()
  y = x - 1
  while y >= 0 and s[y] == ')':
    y -= 1
  # print(y)
  if y + 1 < x - y - 1:
    print("Yes")
  else:
    print("No")
  