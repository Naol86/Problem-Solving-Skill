for _ in range(int(input())):
  n, k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  
  bits = [0] *  31
  for num in nums:
    i = 0
    while num > 0:
      if num & 1:
        bits[i] += 1
      num >>= 1
      i += 1
  i = 30
  while k > 0 and i >= 0:
    need = n - bits[i]
    if need <= k:
      bits[i] += need
      k -= need
    i -= 1
  # print(bits)
  ans = 0
  for i in range(31):
    if bits[i] and bits[i] % n == 0:
      ans += (2**i)
  print(ans)