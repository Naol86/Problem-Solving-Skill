# for _ in range(int(input())):
#   n = int(input())
#   bracket = input()
#   stack = []

#   parent = [i for i in range(2*n)]
#   size = [1] * (2 * n)

#   ans = [2 * n]
#   def find(x):
#     if x == parent[x]:
#       return x
#     parent[x] = find(parent[x])
#     return parent[x]

#   def union(x, y):
#     par_x = find(x)
#     par_y = find(y)
#     if par_x != par_y:
#       ans[0] -= 1
#       if size[par_x] > size[par_y]:
#         parent[par_y] = par_x
#         size[par_x] += size[par_y]
#         return (par_x, 0)
#       else:
#         parent[par_x] = par_y
#         size[par_y] += size[par_x]
#         return (par_y, 0)
    
  
#   i = 0
#   while i < n * 2:
#     if not stack:
#       stack.append(i)
#       i += 1
#     else:
#       if bracket[i] == '(':
#         stack.append(i)
#         i += 1
#       else:
#         if type(stack[-1]) == int:
#           temp = union(stack.pop(), i)
#           while stack and type(stack[-1]) != int:
#             temp = union(stack.pop()[0], temp[0])
#           stack.append(temp)
#           i += 1
#         else:
#           stack.pop()
#   print(ans[0])

for _ in range(int(input())):
  x = int(input())
  ans = x
  s = input()
  i = 0
  while i < x * 2 - 1:
    if s[i] == ')' and s[i+1] == '(':
      i += 2
      ans -= 1
    else:
      i += 1
  print(ans)