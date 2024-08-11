for _ in range(int(input())):
  a, b = map(int, input().split())
  nums = [0] * 52
  _max= 0
  for __ in range(a):
    x, y = map(int, input().split())
    if y < b or x > b:
      continue
    _max = max(_max, x, y)
    nums[x] += 1
    nums[y + 1] -= 1
  for i in range(1, _max + 2):
    nums[i] += nums[i-1]
  temp = nums[b]
  for i in range(_max + 2):
    if i == b:
      continue
    if nums[i] >= temp:
      print("NO")
      break
  else:
    print("YES")
