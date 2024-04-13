def solve():
  st = input().strip()
  n = len(st)
  if "1" not in st:
    print(0)
    return
  l1 = st.index("1")
  r1 = n-1
  while r1 > 0 and st[r1] != "1":
    r1 -= 1
  print(st[l1:r1+1].count("0"))
  
for _ in range(int(input())):
  solve()