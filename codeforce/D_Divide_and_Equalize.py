from typing import Counter


def prime_factor(num):
  i = 2
  ans = []
  while i * i <= num:
    while num % i == 0:
      ans.append(i)
      num //= i
    i += 1
  if num > 1:
    ans.append(num)
  return ans

for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  temp = []
  for num in nums:
    # print(num, prime_factor(num))
    temp.extend(prime_factor(num))
  count = Counter(temp)
  for key, value in count.items():
    if value % x:
      print("NO")
      break
  else:
    print("YES")