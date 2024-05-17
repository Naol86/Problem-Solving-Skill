for _ in range(int(input())):
  x, z = map(int, input().split())
  nums = [int(i) for i in input().split()]
  visited = set()
  ans = 0
  
  while z not in visited:
    _max = 0
    ind = 0
    for i in range(x):
      if z | nums[i] > _max:
        _max = z|nums[i]
        ind = i
      elif z | nums[i] == _max and z & nums[i] > z & nums[ind]:
        ind = i
    visited.add(z)
    nums[ind] = _max
    z = z & nums[i]
    ans = max(ans, _max)
  print(_max)