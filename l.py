from math import *
from sys import stdin
mod = 998244353
input = stdin.readline

def f(m):
  fct = [1]
  for i in range(1, m+1):
    fct.append(i * fct[-1])
  return fct
  
for _ in range(int(input())):
  mod = 998244353
  bs = input().strip()
  
  way = 0
  rem = 0
  # l = 0
  # for r in range(len(bs)):
  #   if bs[r] != bs[l]:
  #     rem += r - l - 1
  #     way *= max(1, r - l)
  #     l = r
  
  # if l != r:
  #   rem = r - l - 1
  #   way *= r - l 
  
  stack = []
  tt = []
  for i in range(len(bs)):
    if (stack and stack[-1] == bs[i] )or not stack:
      stack.append(bs[i])
    else:
      tt.append(len(stack))
      rem += len(stack) - 1
      rem %= mod
      stack = [bs[i]]
  if stack:
    tt.append(len(stack))
    rem += len(stack) - 1
    rem %= mod
  ft = f(max(tt))
  for k in range(len(tt)):
    if ft[tt[k]] == 1:
      continue
    way += ft[tt[k]]
    way %= mod
  if way == 0:
    way = 1
  print(rem, way % mod)
  
  