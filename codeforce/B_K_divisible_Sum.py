def check(n, k):
  if k % n == 0:
    print(k // n)
  else:
    print(k // n + 1)

for _ in range(int(input())):
  n, k = map(int, input().split())
  if n > k:
    rem = n % k
    add = - rem + k
    if rem == 0:
      print(n)
      continue
    x = n
    n += k - rem
    # print('n is', n,k)
    check(x, n)
  else:
    check(n, k)