x = input()
open = []
close = []
for i in range(len(x)):
  if x[i] == ")":
    close.append(i+1)
  else:
    open.append(i+1)
stack = []
count = 0
ans = []
temp = []
left = len(open) - 1
right = len(close) - 1
while(left >= 0 and right >= 0):
  if close[right] > open[left] and not (left == 0 and right == 0):
    temp.append(open[left])
    temp.append(close[right])
    left -= 1
    right -= 1
  else:
    if temp:
      temp.sort()
      ans.append(temp.copy())
    temp = []
    left -= 1
if temp:
  ans.append(temp)
# print(ans)/
print(len(ans))
for i in range(len(ans)):
  print(len(ans[i]))
  print(*ans[i])
    
    
    
    