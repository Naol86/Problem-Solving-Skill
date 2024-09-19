import math


n, m, k = map(int, input().split())
num = 2 * m
lane = (k // num)
if lane != k / num:
  lane += 1
k %= num
desk = k // 2
if k % 2:
  desk += 1
if desk == 0:
  desk = m
if k % 2:
  pos = 'L'
else:
  pos = 'R'

print(lane, desk, pos)