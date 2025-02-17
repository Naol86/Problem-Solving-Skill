n, t = map(int, input().split()) # input cal
#max n = 100
init = 10 ** (n - 1) # log(n)

# 4 3
ans = init + (t - (init % t)) # 1

if ans < 10 ** n: # 1
  print(ans) # 1
else:
  print(-1)