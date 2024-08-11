for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]

  count = 0
  i = 1
  
  visited = set()
  
  for num in nums:
    if num - 1 in visited:
      visited.add(num)
      continue
    visited.add(num)
    count += 1
  
  print(count - 1)