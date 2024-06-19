def solve(n):
  s = input()
  stack = []
  for i in range(len(s)):
    while(stack and stack[-1][0] < s[i]):
      stack.pop()
    stack.append([s[i],i])
  right = len(stack)-1
  left = 0
  while(left < right):
    stack[left][0],stack[right][0] = stack[right][0],stack[left][0]
    right -= 1
    left += 1
  s = list(s)
  for x,y in stack:
    s[y] = x
  minus = 0
  right = len(stack)-2
  while(right >= 0):
    if stack[right][0] != stack[right+1][0]:
      break
    minus += 1
    right -= 1
  # print(stack,"==")
  for x in range(1,len(s)):
    if s[x]  < s[x-1]:
      return -1
  ans = len(stack)-1
  ans -= minus
  return ans
t = int(input())
for _ in range(t):
  n = int(input())
  ans = solve(n)
  print(ans)