for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]


  last = [([0] * 30) for __ in range(x + 1)]
  for i in range(1, x + 1):
    num = nums[i - 1]
    ind = 0
    while num > 0:
      if num & 1:
        last[i][ind] += 1
      ind += 1
      num >>= 1
  # prefix sum
  for i in range(1, x + 1):
    for j in range(30):
      last[i][j] += last[i-1][j]
  def calculate(l, mid):
    _sum = 0
    dis = mid - l + 1
    for i in range(30):
      if last[mid][i] - last[l-1][i] >= dis:
        _sum += (1<<i)
    return _sum
  
  ans = []
  for __ in range(int(input())):
    a, b = map(int, input().split())

    left = a
    right = x
    temp = -1
    while left <= right:
      mid = left + (right - left) // 2
      if calculate(a, mid) >= b:
        temp = mid
        left = mid + 1
      else:
        right = mid - 1
    ans.append(temp)
  print(*ans)
  # print(last)