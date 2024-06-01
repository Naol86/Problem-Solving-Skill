from collections import defaultdict

for _ in range(int(input())):
  n = int(input())
  nms = [int(i) for i in input().split()]
  
  fs = defaultdict(int)
  fl = defaultdict(int)
  sl = defaultdict(int)
  fsl = defaultdict(int)
  
  trip = []
  
  res  =0
  
  for i in range(n-2):
    a,b,c = nms[i], nms[i+1], nms[i+2]
    fs[(a, b)] += 1
    fl[(a, c)] += 1
    sl[(b, c)] += 1
    fsl[(a, b,c)] += 1
    trip.append((a,b,c))
  
  for a, b, c in trip:
    res += fs[(a, b)] - 1 + fl[(a, c) ] + sl[(b, c)] - 2 - 3 * (fsl[(a, b, c)]-1)
  
  print(res//2)