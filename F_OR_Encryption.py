for _ in range(int(input())):
  x = int(input())
  matrix = []
  sum_ = 0
  for __ in range(x):
    nums = [int(i) for i in input().split()]
    sum_ += sum(nums)
    matrix.append(nums)
  if x == 1:
    print("YES")
    print("1")
    continue
  count = 0
  ans = [(2<<31) - 1] * x
  if sum_ == 0:
    print("YES")
    print(*ans)
    continue
  
  for i in range(x):
    for j in range(x):
      count += matrix[i][j]
      if i == j:
        continue
      ans[i] &= matrix[i][j]
      ans[j] &= matrix[i][j]
  if sum(ans) == 0 and count != 0:
    print("NO")
    continue
  print("YES")
  print(*ans)