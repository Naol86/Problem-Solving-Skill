
def counter(s):
  dict = {}
  for i in s:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  return dict

for _ in range(int(input())):
  a, b = input().split()
  
  count = counter(b)
  i = len(a) - 1
  j = len(b) - 1

  while i >= 0 and j >= 0:
    if a[i] == b[j]:
      count[b[j]] -= 1  
      j -= 1
      i -= 1
      continue
    if a[i] in count and count[a[i]] > 0:
      print("NO")
      break
    i-=1
  else:
    if j == -1:
      print("YES")
      continue
    print("NO")

