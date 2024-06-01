def solve():
  stack = [-1]
  n = int(input())
  nums = list(map(int,input().split()))
  nums.append(float('-inf'))
  answer = 0
  ans = [0] * n
  for i in range(n+1):
    count = 0
    while len(stack) > 1 and nums[stack[-1]] > nums[i]:
      count += 1
      ele = stack.pop()
      ans[ele] = (ele - stack[-1]) * (i - ele)
    # print(count,i,ans)
    if i != n:
      ans[stack[-1]] -= count
    # print(ans)
    stack.append(i)
  print(ans)
for _ in range(int(input())):
  solve()