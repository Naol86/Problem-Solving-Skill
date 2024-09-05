def check(lis):
  for i in range(4):
    if lis[i] == '#':
      return i + 1

for _ in range(int(input())):
  x = int(input())
  ans = []
  for __ in range(x):
    lis = input()
    ans.append(check(lis))
  print(*ans[::-1])