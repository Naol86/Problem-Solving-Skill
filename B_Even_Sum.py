for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  _sum = 0
  odd = []
  even = []
  for num in nums:
    _sum += num
    if num % 2:
      odd.append(num)
    else:
      even.append(num)
  if _sum % 2 == 0:
    print(0)
    continue
  else:
    even.sort()
    even_last = float('inf')
    for num in even:
      count = 0
      while num % 2 == 0:
        count += 1
        num //= 2
      even_last = min(even_last, count)
    _min = float('inf')
    for num in odd:
      count = 0
      while num % 2:
        count += 1
        num //= 2
      _min = min(_min, count)
    print(min(_min, even_last))