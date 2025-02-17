from collections import defaultdict


s1 = input()
s2 = input()

hash = defaultdict(lambda: float('inf'))


for _ in range(int(input())):
  a, b, w = input().split()
  # if hash[(a,b)] > int(w):
  hash[(a, b)] = min(hash[(a, b)], int(w))
  

if len(s1) != len(s2):
  print(-1)

else:

  # print(hash)

  cost = 0
  ans = []
  for i in range(len(s1)):
    a = s1[i]
    b = s2[i]
    if a == b:
      ans.append(a)
      continue
    elif ((a, b) in hash) or ((b, a) in hash):
      if hash[(a,b)] < hash[(b,a)]:
        ans.append(b)
        cost += hash[(a, b)]
      else:
        ans.append(a)
        cost += hash[(b, a)]
    else:
      print(-1)
      break
  else:
    print(cost)
    print(''.join(ans))