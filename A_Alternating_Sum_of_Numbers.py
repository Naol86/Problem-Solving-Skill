for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  pro = 0
  one = 1
  for num in nums:
    pro += (num * one)
    one *= -1
  print(pro)