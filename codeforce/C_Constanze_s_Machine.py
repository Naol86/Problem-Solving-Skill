def solve():
  s = f"{input()}x"
  pre = 'o'
  count = 0
  _max = 1
  mul = [1]
  for i in s:
    _max = max(_max, count)
    if i in {'m', 'w'}:
      return 0
    if i in {'n', 'u'}:
      if i == pre:
        count +=1
      else:
        if count > 1:
          mul.append(count)
        count = 1
        pre = i
    else:
      if count > 1:
        mul.append(count)
      pre = i
      count = 0
  nums = [0] * (_max + 1)
  def fibo(n):
    nums[0] = nums[1] = 1
    i = 2
    while i <= n:
      nums[i] += nums[i-1] + nums[i-2]
      i += 1
  fibo(_max)
  ans = 1
  for i in mul:
    ans *= nums[i]
    ans %= (10 ** 9 + 7)
  return ans
print(solve())