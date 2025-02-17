for _ in range(int(input())):
  n, m = map(int, input().split())
  matrix = []
  lis = []
  for i in range(n):
    nums = [int(i) for i in input().split()]
    matrix.append(nums)
    lis.append((sum(nums), i))
  lis.sort(reverse=True)
  # print(lis)
  nums = []
  for i, j in lis:
    nums.extend(matrix[j])
  # print(nums)
  pre = 0
  count = 0
  for num in nums:
    pre += num
    count += pre
  print(count)