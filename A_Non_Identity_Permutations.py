for _ in range(int(input())):
  x = int(input())
  ans = [i for i in range(1, x + 1)]
  if x % 2 == 0:
    print(*ans[::-1])
  else:
    mid = x//2
    ans[0], ans[mid] = ans[mid], ans[0]
    print(*ans[::-1])