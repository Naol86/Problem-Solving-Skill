n = int(input())
l = list(map(int,input().split()))
# l.sort()
odd = []
even = []
for i in l:
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)
ans = []
while(odd or even):
  if odd:
    ans.append(odd.pop())
  if even:
    ans.append(even.pop())
print(*ans)
    