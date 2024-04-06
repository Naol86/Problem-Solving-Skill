from collections import defaultdict
def solve():
  ll = []
  n = int(input())
  j = input().strip()
  cards = [i for i in input().split()]
  d = defaultdict(list)
  jc = []
  for c in cards:
    r, s = int(c[0]), c[1]
    if s == j:
      jc.append(r)
      continue
    d[s].append(r)
  jc.sort()
  for key,val in d.items():
    val.sort()
    while val and val[0] != val[-1]:
      ll.append(f"{val[0]}{key} {val[-1]}{key}")
      val.pop()
      val.pop(0)
    while val and jc:
      ll.append(f"{val[-1]}{key} {jc[-1]}{j}")
      val.pop()
      jc.pop()
    if val:
      return False
  while jc and len(jc) > 1:
    ll.append(f"{jc[0]}{j} {jc[-1]}{j}")
    jc.pop()
    jc.pop(0)
  if jc:
    return False
  return ll

for _ in range(int(input())):
  y = solve()
  if y:
    for a in y:
      print(a)
  else:
    print("IMPOSSIBLE")
      
  
  
  
  