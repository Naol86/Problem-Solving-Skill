for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  prefix = [0]
  for num in nums:
    prefix.append(prefix[-1] + num)
  s = input()
  left = []
  right = []
  for i in range(x):
    x = s[i]
    if x == 'L':
      left.append(i)
    else:
      right.append(i)
  i = 0
  j = len(right) - 1
  ans = 0
  while i < len(left) and j >= 0 and left[i] < right[j]:
    ans += (prefix[right[j] + 1] - prefix[left[i]])
    i += 1
    j -= 1
  # print(left)
  # print(right)
  print(ans)