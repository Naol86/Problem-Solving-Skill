for _ in range(int(input())):
  x = int(input())
  nums = [0] + [int(i) for i in input().split()]
  bits = input()
  zero_one = [0, 0]
  
  for i in range(1, x + 1):
    if bits[i - 1] == '0':
      zero_one[0] ^= nums[i]
    else:
      zero_one[1] ^= nums[i]
    nums[i] ^= nums[i - 1]
  
  ans = []
  for __ in range(int(input())):
    queries = [int(i) for i in input().split()]
    if queries[0] == 2:
      ans.append(zero_one[queries[1]])
    else:
      temp = nums[queries[2]] ^ nums[queries[1] - 1]
      zero_one[0] ^= temp
      zero_one[1] ^= temp
  print(*ans)