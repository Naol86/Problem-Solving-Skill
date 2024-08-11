for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  odd = 0
  for num in nums:
    if num % 2 == 1:
      odd += 1
  if odd != x:
    print("No")
  else:
    print("Yes")