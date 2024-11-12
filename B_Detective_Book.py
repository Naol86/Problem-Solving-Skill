

n = int(input())
nms = [int(i) for i  in input().split()]


ans = 0


mx = nms[0]

i = 0

while i < n:
  mx = max(mx, nms[i])
  if i + 1 == mx:
    ans += 1
  i += 1
    
print(ans)
