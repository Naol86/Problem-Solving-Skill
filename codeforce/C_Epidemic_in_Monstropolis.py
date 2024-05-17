from collections import Counter
ans = []

def solve(part, id):
  def geti(part):
    m = max(part)
    for i in range(len(part)):
      if i > 0 and part[i-1] != m and part[i] == m:
        return i
      if i < len(part)-1 and part[i+1] != m and part[i] == m:
        return i
  
  if len(Counter(part)) == 1:
    return False
  while len(part) > 1:
    n = len(part)
    mx = geti(part)
    if mx < n-1 and part[mx] > part[mx+1]:
      part[mx] += part[mx+1]
      part.pop(mx+1)
      ans.append((id+mx, "R"))
    else:
      part[mx-1] += part[mx]
      part.pop(mx)
      ans.append((id+mx, "L"))
  return True

n = int(input())
nums = [int(i) for i in input().split()]

k = int(input())
fs = [int(i) for i in input().split()]
invalid = False
l = 0
id = 1
for i in range(k):
  s = 0
  part = []
  while l < n and s < fs[i]:
    s += nums[l]
    part.append(nums[l])
    l+=1
  if s > fs[i]:
    invalid = True
    break
  if s < fs[i]:
    invalid = True
    break
  if not solve(part, id):
    invalid = True
    break
  id += 1


if invalid:
  print("NO")
else:
  print("YES")
  for i in ans:
    print(*i)
      
        
        
    