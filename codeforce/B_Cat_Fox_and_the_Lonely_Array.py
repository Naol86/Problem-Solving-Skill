from collections import defaultdict


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  number = 0
  for num in nums:
    number |= num
  count = [0] * 20
  used = 0
  left = 0
  right = 0
  ans = 0
  while right < x:
    j = 0
    num = nums[right]
    while num > 0:
      if num & 1:
        count[j] += 1
        used |= (1<<j)
      num >>= 1
      j += 1
    if used == number:
      ans = max(ans, right - left + 1)
      while left <= right and used == number:
        j = 0
        num = nums[left]
        while left <= right and num > 0:
          if num & 1:
            count[j] -= 1
            if count[j] == 0:
              used ^= (1<<j)
          num >>= 1
          j += 1
        left += 1
    right += 1
  print(ans)